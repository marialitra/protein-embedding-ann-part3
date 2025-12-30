#!/usr/bin/env python3
"""
Generate properly formatted output according to assignment requirements
Includes: Method comparison table, Top-N neighbors with BLAST identity and bio comments
"""

import os
import sys
import csv
from collections import defaultdict

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


def parse_ann_results_with_distances(results_file, topN=50):
    """Parse ANN results and extract neighbor IDs with distances"""
    results = defaultdict(list)
    current_query = None
    
    with open(results_file, 'r') as f:
        for line in f:
            line = line.strip()
            
            if line.startswith('Query:'):
                current_query = line.split('Query:')[1].strip()
            elif line.startswith('Nearest neighbor') and current_query:
                try:
                    parts = line.split(':')[1].strip().split()
                    neighbor_id = parts[0]
                    
                    # Try to extract distance if available (after neighbor ID)
                    distance = None
                    if len(parts) > 1:
                        try:
                            distance = float(parts[1])
                        except:
                            distance = None
                    
                    if len(results[current_query]) < topN:
                        results[current_query].append({
                            'id': neighbor_id,
                            'distance': distance,
                            'rank': len(results[current_query]) + 1
                        })
                except Exception as e:
                    pass
    
    return results


def get_bio_comment(query_id, neighbor_id, blast_identity, in_blast_top, 
                     identity_map, uniprot_cache=None):
    """Generate biological comment for a neighbor"""
    
    # Twilight zone: identity < 30%
    is_twilight = blast_identity is not None and blast_identity < 30.0
    
    if in_blast_top:
        if is_twilight:
            return "Twilight zone homolog (low seq identity, high BLAST rank)"
        else:
            return "BLAST confirmed hit"
    else:
        if is_twilight or blast_identity is None:
            return "Potential remote homolog (not in BLAST top-N, check domains)"
        else:
            return "Novel discovery by embeddings"


def generate_formatted_output(query_id, methods, results_dir, blast_file, 
                               blast_identity_map, N_recall=50, N_display=10):
    """Generate formatted output for a single query according to assignment specs"""
    
    output = []
    output.append(f"\n{'='*100}")
    output.append(f"Query Protein: {query_id}")
    output.append(f"N = {N_recall} (μέγεθος λίστας Top-N για την αξιολόγηση Recall@N)")
    output.append(f"{'='*100}")
    
    # Load BLAST ground truth for this query
    blast_gt = parse_blast_tsv(blast_file, N_recall)
    blast_hits_for_query = blast_gt.get(query_id, set())
    
    # [1] Συνοπτική σύγκριση μεθόδων
    output.append("\n[1] Συνοπτική σύγκριση μεθόδων")
    output.append("-" * 100)
    output.append(f"{'Method':<20} | {'Time/query (s)':<15} | {'QPS':<10} | {'Recall@N vs BLAST Top-N':<25}")
    output.append("-" * 100)
    
    # Extract metrics for each method
    method_metrics = {}
    
    for method in methods:
        results_file = os.path.join(results_dir, f"results_{method}.txt")
        if not os.path.exists(results_file):
            continue
        
        # Compute recall for this method
        mean_recall, per_query = compute_recall(blast_file, results_file, N_recall)
        query_recall = per_query.get(query_id, 0.0)
        
        # Get QPS (from previous runs - you may need to extract from output)
        # For now, using stored values from last run
        qps_values = {
            'lsh': 0.7010,
            'hypercube': 19.6176,
            'ivfflat': 1.5543,
            'ivfpq': 12.2624,
            'nlsh': 71.2496
        }
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
        
        output.append(f"{method_display:<20} | {time_per_query:>15.4f} | {qps:>10.2f} | {query_recall:>25.2f}")
    
    # Add BLAST reference
    output.append(f"{'BLAST (Reference)':<20} | {1.500:>15.3f} | {0.67:>10.2f} | {1.00:>25.2f} (ορίζει το Top-N)")
    output.append("-" * 100)
    
    # [2] Top-N γείτονες ανά μέθοδο
    output.append(f"\n[2] Top-N γείτονες ανά μέθοδο (N = {N_display} για εκτύπωση)")
    output.append("=" * 100)
    
    for method in methods:
        results_file = os.path.join(results_dir, f"results_{method}.txt")
        if not os.path.exists(results_file):
            continue
        
        # Parse ANN results
        ann_results = parse_ann_results_with_distances(results_file, N_recall)
        
        if query_id not in ann_results:
            continue
        
        neighbors = ann_results[query_id][:N_display]
        
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
        
        output.append(f"\nMethod: {method_display}")
        output.append("-" * 120)
        output.append(f"{'Rank':<6} | {'Neighbor ID':<15} | {'Distance':<10} | {'BLAST Identity':<15} | {'In BLAST Top-N?':<18} | {'Bio comment':<40}")
        output.append("-" * 120)
        
        for neighbor in neighbors:
            neighbor_id = neighbor['id']
            rank = neighbor['rank']
            distance = neighbor.get('distance', 'N/A')
            
            # Get BLAST identity
            blast_identity = blast_identity_map.get(query_id, {}).get(neighbor_id, None)
            blast_identity_str = f"{blast_identity:.1f}%" if blast_identity is not None else "N/A"
            
            # Check if in BLAST top-N
            in_blast = neighbor_id in blast_hits_for_query
            in_blast_str = "Yes" if in_blast else "No"
            
            # Generate bio comment
            bio_comment = get_bio_comment(query_id, neighbor_id, blast_identity, 
                                          in_blast, blast_identity_map)
            
            # Format distance
            dist_str = f"{distance:.4f}" if distance is not None else "N/A"
            
            output.append(f"{rank:<6} | {neighbor_id:<15} | {dist_str:<10} | {blast_identity_str:<15} | {in_blast_str:<18} | {bio_comment:<40}")
        
        output.append("")
    
    return "\n".join(output)


def main():
    """Generate formatted output for all queries"""
    
    # Configuration
    QUERY_FASTA = "Data/targets.fasta"
    BLAST_FILE = "output/blast/search/blast_results.tsv"
    BLAST_TOPN_FILE = "output/blast/topN/blast_results_top5.tsv"
    RESULTS_DIR = "output/search"
    METHODS = ['lsh', 'hypercube', 'ivfflat', 'ivfpq', 'nlsh']
    OUTPUT_FILE = "output/evaluation/formatted_results.txt"
    N_RECALL = 50  # For recall calculation
    N_DISPLAY = 10  # For display in output
    
    # Parse BLAST identities
    print("Parsing BLAST identities...")
    blast_identity_map = parse_blast_identity(BLAST_FILE)
    
    # Get list of queries
    from protein_search import parse_blast_tsv
    blast_gt = parse_blast_tsv(BLAST_TOPN_FILE, 5)
    queries = sorted(blast_gt.keys())
    
    print(f"Generating formatted output for {len(queries)} queries...")
    
    all_output = []
    all_output.append("="*100)
    all_output.append("ASSIGNMENT OUTPUT: Approximate Nearest Neighbor Search for Remote Homologs")
    all_output.append("Using ESM-2 Embeddings and Multiple ANN Methods")
    all_output.append("="*100)
    
    for query_id in queries:
        output = generate_formatted_output(
            query_id, 
            METHODS, 
            RESULTS_DIR, 
            BLAST_FILE,
            blast_identity_map,
            N_RECALL,
            N_DISPLAY
        )
        all_output.append(output)
    
    # Write to file
    output_text = "\n".join(all_output)
    with open(OUTPUT_FILE, 'w') as f:
        f.write(output_text)
    
    print(f"\n✅ Formatted output saved to: {OUTPUT_FILE}")
    
    # Print first query as sample
    print("\n" + "="*100)
    print("SAMPLE OUTPUT (First Query):")
    print("="*100)
    
    if queries:
        sample = generate_formatted_output(
            queries[0], 
            METHODS, 
            RESULTS_DIR, 
            BLAST_FILE,
            blast_identity_map,
            N_RECALL,
            N_DISPLAY
        )
        print(sample)


if __name__ == "__main__":
    main()
