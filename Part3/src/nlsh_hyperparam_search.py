#!/usr/bin/env python3
"""
NLSH Hyperparameter Search Script
Tests different combinations of NLSH hyperparameters and saves results to CSV
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
    # Search params (affect search only, not index build)
    T,
    # Build params (affect index build - requires rebuild)
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
    config_name = f"T{T}_m{m}_imb{imbalance}_layers{layers}_nodes{nodes}_epochs{epochs}"
    run_dir = os.path.join(output_dir, config_name)
    os.makedirs(run_dir, exist_ok=True)
    
    index_dir = os.path.join(run_dir, "index")
    output_txt = os.path.join(run_dir, "results.txt")
    
    # If rebuild_index is True, remove existing index
    if rebuild_index and os.path.exists(index_dir):
        print(f"  [Removing old index at {index_dir}]")
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
    
    print(f"\n{'='*70}")
    print(f"Testing: {config_name}")
    print(f"{'='*70}")
    
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
            if 'QPS result:' in line:
                # Look for the next line with the actual QPS value
                continue
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
                print(f"  [Error computing recall: {e}]")
        
        print(f"  Results: Recall={recall:.4f}, QPS={qps}")
        
        # Clean up query files
        query_dat = output_txt.replace('.txt', '.queries.dat')
        query_ids = output_txt.replace('.txt', '.queries_ids.txt')
        for f in [query_dat, query_ids]:
            if os.path.exists(f):
                os.remove(f)
        
        return {
            'config': config_name,
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
            'success': True
        }
        
    except Exception as e:
        print(f"  [ERROR: {e}]")
        return {
            'config': config_name,
            'T': T,
            'm': m,
            'imbalance': imbalance,
            'kahip_mode': kahip_mode,
            'layers': layers,
            'nodes': nodes,
            'epochs': epochs,
            'batch_size': batch_size,
            'lr': lr,
            'recall': 0.0,
            'qps': 0.0,
            'success': False
        }


def main():
    # Configuration
    BASE_DAT = "output/embeddings/vectors_50k_opt.dat"
    QUERY_FASTA = "Data/targets.fasta"
    OUTPUT_DIR = "output/nlsh_hyperparam_search"
    BLAST_RESULTS = "output/blast/topN/blast_results_top5.tsv"
    N = 5
    SEED = 42
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Define hyperparameter search space
    # Search parameters (don't require index rebuild)
    T_values = [50, 100, 200, 300, 500]  # Number of bins to probe
    
    # Build parameters (require index rebuild)
    # Starting with smaller search space, can expand based on results
    m_values = [1000, 2000, 4000]  # Number of partitions for KaHIP
    imbalance_values = [0.05, 0.1, 0.2]  # KaHIP imbalance factor
    layer_values = [2, 3, 4]  # MLP layers
    node_values = [128, 256, 512]  # MLP hidden units
    epoch_values = [3, 5, 10]  # Training epochs
    
    # Keep these fixed for now
    kahip_mode = 0
    batch_size = 512
    lr = 1e-3
    
    print("="*70)
    print("NLSH Hyperparameter Search")
    print("="*70)
    print(f"Base dataset: {BASE_DAT}")
    print(f"Query file: {QUERY_FASTA}")
    print(f"Output directory: {OUTPUT_DIR}")
    print(f"N (neighbors): {N}")
    print(f"\nSearch space:")
    print(f"  T: {T_values}")
    print(f"  m: {m_values}")
    print(f"  imbalance: {imbalance_values}")
    print(f"  layers: {layer_values}")
    print(f"  nodes: {node_values}")
    print(f"  epochs: {epoch_values}")
    
    # Generate all combinations for build parameters
    build_combinations = list(product(m_values, imbalance_values, layer_values, node_values, epoch_values))
    
    print(f"\nTotal build configurations: {len(build_combinations)}")
    print(f"Search configurations per build: {len(T_values)}")
    print(f"Total experiments: {len(build_combinations) * len(T_values)}")
    print("="*70)
    
    results = []
    
    # For each build configuration, test all T values
    for i, (m, imbalance, layers, nodes, epochs) in enumerate(build_combinations, 1):
        print(f"\n\nBuild Config {i}/{len(build_combinations)}")
        print(f"m={m}, imbalance={imbalance}, layers={layers}, nodes={nodes}, epochs={epochs}")
        
        for j, T in enumerate(T_values, 1):
            print(f"\n  Search Config {j}/{len(T_values)} (T={T})")
            
            # First search with this build config requires rebuild
            rebuild = (j == 1)
            
            result = run_nlsh_with_params(
                base_dat=BASE_DAT,
                query_fasta=QUERY_FASTA,
                output_dir=OUTPUT_DIR,
                blast_results=BLAST_RESULTS,
                N=N,
                seed=SEED,
                T=T,
                m=m,
                imbalance=imbalance,
                kahip_mode=kahip_mode,
                layers=layers,
                nodes=nodes,
                epochs=epochs,
                batch_size=batch_size,
                lr=lr,
                rebuild_index=rebuild
            )
            
            results.append(result)
            
            # Save intermediate results after each experiment
            csv_file = os.path.join(OUTPUT_DIR, "nlsh_hyperparam_results.csv")
            with open(csv_file, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=[
                    'config', 'T', 'm', 'imbalance', 'kahip_mode',
                    'layers', 'nodes', 'epochs', 'batch_size', 'lr',
                    'recall', 'qps', 'success'
                ])
                writer.writeheader()
                writer.writerows(results)
    
    # Print summary
    print("\n" + "="*70)
    print("HYPERPARAMETER SEARCH COMPLETE")
    print("="*70)
    
    # Sort by recall
    successful_results = [r for r in results if r['success']]
    successful_results.sort(key=lambda x: x['recall'], reverse=True)
    
    print(f"\nTop 10 configurations by recall:")
    print(f"{'Rank':<6} {'Recall':<8} {'QPS':<10} {'Config'}")
    print("-"*70)
    for i, r in enumerate(successful_results[:10], 1):
        print(f"{i:<6} {r['recall']:<8.4f} {r['qps']:<10.2f} {r['config']}")
    
    print(f"\nFull results saved to: {csv_file}")
    print(f"Best recall: {successful_results[0]['recall']:.4f}")
    print(f"Best config: T={successful_results[0]['T']}, m={successful_results[0]['m']}, "
          f"imbalance={successful_results[0]['imbalance']}, layers={successful_results[0]['layers']}, "
          f"nodes={successful_results[0]['nodes']}, epochs={successful_results[0]['epochs']}")


if __name__ == "__main__":
    main()
