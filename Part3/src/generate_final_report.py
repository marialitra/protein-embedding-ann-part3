#!/usr/bin/env python3
"""
Generate final formatted report according to assignment requirements.
Uses precomputed distances and BLAST identities.
"""

import os
import sys
import csv
from collections import defaultdict
from pathlib import Path

sys.path.append(os.path.dirname(__file__))
from protein_search import parse_blast_tsv, compute_recall


def parse_blast_identity(blast_file):
    """Extract BLAST identity % for each query-target pair"""
    identity_map = defaultdict(dict)
    
    with open(blast_file, 'r') as f:
        for line in f:
            if not line.strip():
                continue
            cols = line.strip().split('\t')
            query_id = cols[0]
            target_field = cols[1]
            identity_pct = float(cols[2])
            
            # Extract target ID from sp|ID|...
            if target_field.startswith('sp|'):
                target_id = target_field.split('|')[1]
            else:
                target_id = target_field
            
            identity_map[query_id][target_id] = identity_pct
    
    return identity_map


def parse_ann_results(results_file, topN=50):
    """Parse ANN results and extract neighbor IDs"""
    results = defaultdict(list)
    current_query = None
    
    with open(results_file, 'r') as f:
        for line in f:
            line = line.strip()
            
            if line.startswith('Query:'):
                current_query = line.split('Query:')[1].strip()
            elif line.startswith('Nearest neighbor-'):
                if current_query:
                    neighbor_id = line.split(':')[1].strip()
                    if len(results[current_query]) < topN:
                        results[current_query].append(neighbor_id)
    
    return results


def parse_distances(distances_file):
    """Parse distances file and return {query_id: {neighbor_id: distance}}"""
    distances = defaultdict(dict)
    current_query = None
    
    with open(distances_file, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            
            if line.startswith('Query:'):
                current_query = line.split('Query:')[1].strip()
            elif line.startswith('Neighbor-') and current_query:
                # Format: "Neighbor-1: ID | Distance: 0.0123"
                parts = line.split('|')
                neighbor_id = parts[0].split(':')[1].strip()
                if len(parts) > 1:
                    try:
                        distance = float(parts[1].split(':')[1].strip())
                        distances[current_query][neighbor_id] = distance
                    except:
                        pass
    
    return distances


def get_bio_comment(query_id, neighbor_id, blast_identity, in_blast):
    """Generate biological comment for a neighbor"""
    
    # Twilight zone: identity < 30%
    is_twilight = blast_identity is not None and blast_identity < 30.0
    
    if in_blast:
        if is_twilight:
            return "Twilight zone homolog (identity <30%, high BLAST rank)"
        else:
            return "BLAST confirmed hit"
    else:
        if is_twilight or blast_identity is None:
            return "Potential remote homolog (not in BLAST top-N)"
        else:
            return "Novel discovery by embeddings"


def generate_formatted_output(query_id, methods, results_dir, distances_dir, 
                               blast_file, blast_identity_map, N_recall=50, N_display=10):
    """Generate formatted output for a single query"""
    
    output = []
    output.append(f"\n{'='*110}")
    output.append(f"Query Protein: {query_id}")
    output.append(f"N = {N_recall} (μέγεθος λίστας Top-N για την αξιολόγηση Recall@N)")
    output.append(f"{'='*110}")
    
    # Load BLAST ground truth for this query
    blast_gt = parse_blast_tsv(blast_file, N_recall)
    blast_hits_for_query = blast_gt.get(query_id, set())
    
    # [1] Συνοπτική σύγκριση μεθόδων
    output.append("\n[1] Συνοπτική σύγκριση μεθόδων")
    output.append("-" * 110)
    output.append(f"{'Method':<18} | {'Time/query (s)':<15} | {'QPS':<10} | {'Recall@N':<12}")
    output.append("-" * 110)
    
    # QPS values from previous measurements
    qps_values = {
        'lsh': 0.7010,
        'hypercube': 19.6176,
        'ivfflat': 1.5543,
        'ivfpq': 12.2624,
        'nlsh': 71.2496
    }
    
    # Extract metrics for each method
    method_metrics = {}
    
    for method in methods:
        results_file = os.path.join(results_dir, f"results_{method}.txt")
        if not os.path.exists(results_file):
            continue
        
        # Compute recall for this method
        mean_recall, per_query = compute_recall(blast_file, results_file, N_recall)
        query_recall = per_query.get(query_id, 0.0)
        
        # Get QPS
        qps = qps_values.get(method, 0.0)
        time_per_query = 1.0 / qps if qps > 0 else 0.0
        
        method_metrics[method] = {
            'time_per_query': time_per_query,
            'qps': qps,
            'recall': query_recall
        }
        
        # Format method name
        method_display = method.upper()
        if method == 'ivfflat':
            method_display = 'IVF-Flat'
        elif method == 'ivfpq':
            method_display = 'IVF-PQ'
        elif method == 'nlsh':
            method_display = 'Neural LSH'
        elif method == 'hypercube':
            method_display = 'Hypercube'
        elif method == 'lsh':
            method_display = 'Euclidean LSH'
        
        output.append(f"{method_display:<18} | {time_per_query:>15.4f} | {qps:>10.2f} | {query_recall:>12.1%}")
    
    # Add BLAST reference
    output.append(f"{'BLAST (Reference)':<18} | {1.500:>15.3f} | {0.67:>10.2f} | {100.0:>12.1%}")
    output.append("-" * 110)
    
    # [2] Top-N γείτονες ανά μέθοδο
    output.append(f"\n[2] Top-{N_display} γείτονες ανά μέθοδο")
    output.append("=" * 110)
    
    for method in methods:
        results_file = os.path.join(results_dir, f"results_{method}.txt")
        distances_file = os.path.join(distances_dir, f"distances_results_{method}.txt")
        
        if not os.path.exists(results_file) or not os.path.exists(distances_file):
            continue
        
        # Parse ANN results and distances
        ann_results = parse_ann_results(results_file, N_recall)
        distances_map = parse_distances(distances_file)
        
        if query_id not in ann_results:
            continue
        
        neighbors = ann_results[query_id][:N_display]
        query_distances = distances_map.get(query_id, {})
        
        # Format method name
        method_display = method.upper()
        if method == 'ivfflat':
            method_display = 'IVF-Flat'
        elif method == 'ivfpq':
            method_display = 'IVF-PQ'
        elif method == 'nlsh':
            method_display = 'Neural LSH'
        elif method == 'lsh':
            method_display = 'Euclidean LSH'
        
        output.append(f"\n📊 Method: {method_display}")
        output.append("-" * 110)
        output.append(f"{'Rank':<5} | {'Neighbor ID':<12} | {'Cosine Dist':<12} | {'BLAST %':<8} | {'BLAST Hit?':<11} | {'Bio Comment':<50}")
        output.append("-" * 110)
        
        for rank, neighbor_id in enumerate(neighbors, 1):
            # Get distance
            distance = query_distances.get(neighbor_id, None)
            dist_str = f"{distance:.4f}" if distance is not None else "N/A"
            
            # Get BLAST identity
            blast_identity = blast_identity_map.get(query_id, {}).get(neighbor_id, None)
            blast_identity_str = f"{blast_identity:.1f}%" if blast_identity is not None else "N/A"
            
            # Check if in BLAST top-N
            in_blast = neighbor_id in blast_hits_for_query
            in_blast_str = "✓ Yes" if in_blast else "✗ No"
            
            # Generate bio comment
            bio_comment = get_bio_comment(query_id, neighbor_id, blast_identity, in_blast)
            
            output.append(f"{rank:<5} | {neighbor_id:<12} | {dist_str:<12} | {blast_identity_str:<8} | {in_blast_str:<11} | {bio_comment:<50}")
        
        output.append("")
    
    return "\n".join(output)


def main():
    """Generate final formatted report"""
    
    # Configuration
    BLAST_FILE = "output/blast/search/blast_results.tsv"
    BLAST_TOPN_FILE = "output/blast/topN/blast_results_top5.tsv"
    RESULTS_DIR = "output/search"
    DISTANCES_DIR = "output/evaluation"
    METHODS = ['lsh', 'hypercube', 'ivfflat', 'ivfpq', 'nlsh']
    OUTPUT_FILE = "output/evaluation/FINAL_FORMATTED_REPORT.txt"
    N_RECALL = 50  # For recall calculation
    N_DISPLAY = 10  # For display in output
    
    # Change to Part3 directory
    os.chdir(Path(__file__).parent.parent)
    
    print("Generating final formatted report...")
    
    # Parse BLAST identities
    print("📖 Parsing BLAST identities...")
    blast_identity_map = parse_blast_identity(BLAST_FILE)
    
    # Get list of queries
    blast_gt = parse_blast_tsv(BLAST_TOPN_FILE, 5)
    queries = sorted(blast_gt.keys())
    
    print(f"📊 Processing {len(queries)} queries with {len(METHODS)} methods...")
    
    all_output = []
    all_output.append("=" * 110)
    all_output.append("ASSIGNMENT 3 OUTPUT: Remote Homolog Discovery via Approximate Nearest Neighbor Search")
    all_output.append("ESM-2 Embeddings + Multiple ANN Methods (LSH, Hypercube, IVF-Flat, IVF-PQ, Neural LSH)")
    all_output.append("=" * 110)
    
    for i, query_id in enumerate(queries, 1):
        print(f"  [{i}/{len(queries)}] Processing query: {query_id}")
        output = generate_formatted_output(
            query_id, 
            METHODS, 
            RESULTS_DIR,
            DISTANCES_DIR,
            BLAST_FILE,
            blast_identity_map,
            N_RECALL,
            N_DISPLAY
        )
        all_output.append(output)
    
    # Add footer
    all_output.append(f"\n{'='*110}")
    all_output.append("End of Report")
    all_output.append(f"{'='*110}")
    
    # Write to file
    output_text = "\n".join(all_output)
    with open(OUTPUT_FILE, 'w') as f:
        f.write(output_text)
    
    print(f"\n✅ Final formatted report saved to: {OUTPUT_FILE}")
    print(f"📄 Report contains results for {len(queries)} queries with {len(METHODS)} methods")
    
    # Print first query as sample
    if queries:
        print("\n" + "=" * 110)
        print("SAMPLE (First Query):")
        print("=" * 110)
        sample = generate_formatted_output(
            queries[0], 
            METHODS, 
            RESULTS_DIR,
            DISTANCES_DIR,
            BLAST_FILE,
            blast_identity_map,
            N_RECALL,
            N_DISPLAY
        )
        lines = sample.split('\n')
        # Print first 60 lines
        for line in lines[:60]:
            print(line)
        print(f"\n[... ({len(lines) - 60} more lines) ...]")


if __name__ == "__main__":
    main()
