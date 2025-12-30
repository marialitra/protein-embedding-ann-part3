#!/usr/bin/env python3
"""
NLSH Hyperparameter Search Script - Quick Test Version
Tests a smaller subset of hyperparameters quickly
"""

import os
import sys
import csv
import subprocess
import shutil
from itertools import product
from datetime import datetime

# Add parent directory to path
sys.path.append(os.path.dirname(__file__))
from protein_search import parse_blast_tsv, parse_ann_txt, compute_recall


def run_nlsh_with_params(
    base_dat,
    query_fasta,
    output_dir,
    blast_results,
    N,
    seed,
    T,
    m,
    imbalance,
    kahip_mode,
    layers,
    nodes,
    epochs,
    batch_size,
    lr,
    rebuild_index=False
):
    """Run NLSH with specific hyperparameters and return recall + QPS"""
    
    # Create unique output directory for this config
    config_name = f"T{T}_m{m}_imb{imbalance}_L{layers}_N{nodes}_E{epochs}"
    run_dir = os.path.join(output_dir, config_name)
    os.makedirs(run_dir, exist_ok=True)
    
    index_dir = os.path.join(run_dir, "index")
    output_txt = os.path.join(run_dir, "results.txt")
    
    # If rebuild_index is True, remove existing index
    if rebuild_index and os.path.exists(index_dir):
        print(f"    [Removing old index]")
        shutil.rmtree(index_dir)
    
    # Run protein_search with nlsh method
    cmd = [
        sys.executable,
        os.path.join(os.path.dirname(__file__), "protein_search.py"),
        "-d", base_dat,
        "-q", query_fasta,
        "-o", output_txt,
        "-method", "nlsh",
        "-N", str(N),
        "--seed", str(seed),
        "--nlsh-index", index_dir,
        "--nlsh-T", str(T),
        "--nlsh-m", str(m),
        "--nlsh-imbalance", str(imbalance),
        "--nlsh-kahip-mode", str(kahip_mode),
        "--nlsh-layers", str(layers),
        "--nlsh-nodes", str(nodes),
        "--nlsh-epochs", str(epochs),
        "--nlsh-batch-size", str(batch_size),
        "--nlsh-lr", str(lr),
    ]
    
    print(f"  Testing: T={T}, m={m}, imb={imbalance}, L={layers}, N={nodes}, E={epochs}", end=" ... ")
    
    try:
        # Run the search
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            check=False,
            cwd=os.path.dirname(os.path.dirname(__file__))
        )
        
        # Extract QPS from output
        qps = None
        for line in result.stdout.split('\n'):
            if 'Nlsh' in line and ':' in line:
                try:
                    qps = float(line.split(':')[1].strip())
                except:
                    pass
        
        # Compute recall
        recall = 0.0
        if os.path.exists(output_txt):
            try:
                mean_recall, _ = compute_recall(blast_results, output_txt, N)
                recall = mean_recall
            except Exception as e:
                print(f"Error: {e}")
                return None
        
        print(f"Recall={recall:.4f}, QPS={qps:.2f}" if qps else f"Recall={recall:.4f}")
        
        # Clean up query files
        query_dat = output_txt.replace('.txt', '.queries.dat')
        query_ids = output_txt.replace('.txt', '.queries_ids.txt')
        for f in [query_dat, query_ids]:
            if os.path.exists(f):
                os.remove(f)
        
        return {
            'T': T,
            'm': m,
            'imbalance': imbalance,
            'kahip_mode': kahip_mode,
            'layers': layers,
            'nodes': nodes,
            'epochs': epochs,
            'batch_size': batch_size,
            'lr': lr,
            'recall': recall,
            'qps': qps if qps is not None else 0.0,
        }
        
    except Exception as e:
        print(f"ERROR: {e}")
        return None


def main():
    # Configuration
    BASE_DAT = "output/embeddings/vectors_50k_opt.dat"
    QUERY_FASTA = "Data/targets.fasta"
    OUTPUT_DIR = "output/nlsh_hyperparam_search_quick"
    BLAST_RESULTS = "output/blast/topN/blast_results_top5.tsv"
    N = 5
    SEED = 42
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Define hyperparameter search space - QUICK TEST VERSION
    # Test only the most promising variations
    
    # Search parameter: T (number of bins to probe)
    # Current default is 300, let's test around that
    T_values = [200, 300, 400, 500]
    
    # Build parameters - test variations one at a time
    # Baseline: m=2000, imbalance=0.1, layers=3, nodes=256, epochs=5
    
    configs_to_test = [
        # Baseline
        {'m': 2000, 'imbalance': 0.1, 'layers': 3, 'nodes': 256, 'epochs': 5},
        
        # Vary m (number of partitions)
        {'m': 1000, 'imbalance': 0.1, 'layers': 3, 'nodes': 256, 'epochs': 5},
        {'m': 4000, 'imbalance': 0.1, 'layers': 3, 'nodes': 256, 'epochs': 5},
        
        # Vary imbalance
        {'m': 2000, 'imbalance': 0.05, 'layers': 3, 'nodes': 256, 'epochs': 5},
        {'m': 2000, 'imbalance': 0.2, 'layers': 3, 'nodes': 256, 'epochs': 5},
        
        # Vary layers
        {'m': 2000, 'imbalance': 0.1, 'layers': 2, 'nodes': 256, 'epochs': 5},
        {'m': 2000, 'imbalance': 0.1, 'layers': 4, 'nodes': 256, 'epochs': 5},
        
        # Vary nodes
        {'m': 2000, 'imbalance': 0.1, 'layers': 3, 'nodes': 128, 'epochs': 5},
        {'m': 2000, 'imbalance': 0.1, 'layers': 3, 'nodes': 512, 'epochs': 5},
        
        # Vary epochs
        {'m': 2000, 'imbalance': 0.1, 'layers': 3, 'nodes': 256, 'epochs': 3},
        {'m': 2000, 'imbalance': 0.1, 'layers': 3, 'nodes': 256, 'epochs': 10},
    ]
    
    kahip_mode = 0
    batch_size = 512
    lr = 1e-3
    
    print("="*70)
    print("NLSH Hyperparameter Search - Quick Test")
    print("="*70)
    print(f"Base dataset: {BASE_DAT}")
    print(f"Query file: {QUERY_FASTA}")
    print(f"Output directory: {OUTPUT_DIR}")
    print(f"N (neighbors): {N}")
    print(f"\nTesting {len(configs_to_test)} build configs × {len(T_values)} T values = {len(configs_to_test) * len(T_values)} experiments")
    print("="*70)
    
    results = []
    
    # Test each build configuration with all T values
    for i, config in enumerate(configs_to_test, 1):
        print(f"\nBuild Config {i}/{len(configs_to_test)}: m={config['m']}, imb={config['imbalance']}, "
              f"layers={config['layers']}, nodes={config['nodes']}, epochs={config['epochs']}")
        
        for j, T in enumerate(T_values):
            # First T value for this build config requires rebuild
            rebuild = (j == 0)
            
            result = run_nlsh_with_params(
                base_dat=BASE_DAT,
                query_fasta=QUERY_FASTA,
                output_dir=OUTPUT_DIR,
                blast_results=BLAST_RESULTS,
                N=N,
                seed=SEED,
                T=T,
                rebuild_index=rebuild,
                **config,
                kahip_mode=kahip_mode,
                batch_size=batch_size,
                lr=lr
            )
            
            if result:
                results.append(result)
    
    # Save results to CSV
    csv_file = os.path.join(OUTPUT_DIR, "nlsh_hyperparam_results.csv")
    with open(csv_file, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=[
            'T', 'm', 'imbalance', 'kahip_mode',
            'layers', 'nodes', 'epochs', 'batch_size', 'lr',
            'recall', 'qps'
        ])
        writer.writeheader()
        writer.writerows(results)
    
    # Print summary
    print("\n" + "="*70)
    print("QUICK TEST COMPLETE")
    print("="*70)
    
    # Sort by recall
    results.sort(key=lambda x: x['recall'], reverse=True)
    
    print(f"\nTop 5 configurations by recall:")
    print(f"{'Rank':<6} {'Recall':<8} {'QPS':<10} {'T':<5} {'m':<6} {'imb':<6} {'L':<4} {'N':<5} {'E':<4}")
    print("-"*70)
    for i, r in enumerate(results[:5], 1):
        print(f"{i:<6} {r['recall']:<8.4f} {r['qps']:<10.2f} {r['T']:<5} {r['m']:<6} "
              f"{r['imbalance']:<6.2f} {r['layers']:<4} {r['nodes']:<5} {r['epochs']:<4}")
    
    print(f"\nFull results saved to: {csv_file}")
    if results:
        best = results[0]
        print(f"Best recall: {best['recall']:.4f}")
        print(f"Best config: T={best['T']}, m={best['m']}, imbalance={best['imbalance']}, "
              f"layers={best['layers']}, nodes={best['nodes']}, epochs={best['epochs']}")


if __name__ == "__main__":
    main()
