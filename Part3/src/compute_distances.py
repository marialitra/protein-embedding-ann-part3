#!/usr/bin/env python3
"""
Compute cosine distances between query proteins and their ANN neighbors.
Reads embeddings and ANN results, outputs distances.
"""

import numpy as np
import struct
from pathlib import Path
import sys

def read_embeddings_memmap(dat_file, ids_file):
    """
    Read embeddings from memmap binary file (pure 320-dim vectors).
    IDs are in a separate text file.
    
    Args:
        dat_file: Path to the .dat file (e.g., output/embeddings/vectors_50k_opt.dat)
        ids_file: Path to the IDs file
    
    Returns:
        dict: {protein_id: embedding_vector}
    """
    # Configuration
    EMBED_DIM = 320
    
    # Load embeddings memmap (pure float32 vectors)
    data = np.memmap(dat_file, dtype='float32', mode='r')
    num_proteins = len(data) // EMBED_DIM
    embeddings = data.reshape(num_proteins, EMBED_DIM)
    
    # Load protein IDs from text file
    protein_ids = read_protein_ids(ids_file)
    
    if len(protein_ids) != num_proteins:
        print(f"Warning: Mismatch between embeddings ({num_proteins}) and IDs ({len(protein_ids)})")
    
    # Create mapping
    id_to_embedding = {protein_ids[i]: embeddings[i] for i in range(min(len(protein_ids), num_proteins))}
    
    return id_to_embedding


def read_protein_ids(filepath):
    """Read protein IDs from text file."""
    with open(filepath, 'r') as f:
        return [line.strip() for line in f if line.strip()]


def cosine_distance(vec1, vec2):
    """
    Compute cosine distance (1 - cosine_similarity).
    Range: [0, 2], where 0 = identical, 2 = opposite
    """
    dot_product = np.dot(vec1, vec2)
    norm1 = np.linalg.norm(vec1)
    norm2 = np.linalg.norm(vec2)
    
    if norm1 == 0 or norm2 == 0:
        return 1.0  # orthogonal
    
    cosine_sim = dot_product / (norm1 * norm2)
    cosine_sim = np.clip(cosine_sim, -1.0, 1.0)  # numerical stability
    return 1.0 - cosine_sim


def l2_distance(vec1, vec2):
    """Compute Euclidean (L2) distance."""
    return np.linalg.norm(vec1 - vec2)


def parse_ann_results(filepath):
    """
    Parse ANN results file.
    Returns dict: {query_id: [neighbor1, neighbor2, ...]}
    """
    results = {}
    current_query = None
    
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if not line or line in ['LSH', 'HYPERCUBE', 'IVF-Flat', 'IVF-PQ', 'Neural LSH']:
                continue
            
            if line.startswith('Query:'):
                current_query = line.split('Query:')[1].strip()
                results[current_query] = []
            elif line.startswith('Nearest neighbor-'):
                neighbor = line.split(':')[1].strip()
                if current_query:
                    results[current_query].append(neighbor)
    
    return results


def compute_distances_for_method_with_embeddings(method_name, results_file, all_embeddings, distance_type='cosine'):
    """
    Compute distances for all query-neighbor pairs in ANN results.
    
    Args:
        method_name: Name of the method (e.g., 'LSH')
        results_file: Path to ANN results file
        all_embeddings: Dict of protein_id -> embedding_vector (includes queries + dataset)
        distance_type: 'cosine' or 'l2'
    
    Returns:
        dict: {query_id: [(neighbor_id, distance), ...]}
    """
    print(f"\n{'='*80}")
    print(f"Computing distances for {method_name}")
    print(f"{'='*80}")
    
    # Parse ANN results
    print(f"Parsing ANN results from {results_file}...")
    ann_results = parse_ann_results(results_file)
    print(f"Found results for {len(ann_results)} queries")
    
    # Compute distances
    distances = {}
    distance_func = cosine_distance if distance_type == 'cosine' else l2_distance
    
    for query_id, neighbors in ann_results.items():
        if query_id not in all_embeddings:
            print(f"Warning: Query {query_id} not found in embeddings")
            continue
        
        query_vec = all_embeddings[query_id]
        distances[query_id] = []
        
        for neighbor_id in neighbors:
            if neighbor_id not in all_embeddings:
                print(f"Warning: Neighbor {neighbor_id} not found in embeddings")
                distances[query_id].append((neighbor_id, float('inf')))
                continue
            
            neighbor_vec = all_embeddings[neighbor_id]
            dist = distance_func(query_vec, neighbor_vec)
            distances[query_id].append((neighbor_id, dist))
    
    return distances


def save_distances(distances, output_file):
    """Save distances to text file."""
    with open(output_file, 'w') as f:
        for query_id, neighbor_distances in distances.items():
            f.write(f"Query: {query_id}\n")
            for rank, (neighbor_id, dist) in enumerate(neighbor_distances, 1):
                f.write(f"Neighbor-{rank}: {neighbor_id} | Distance: {dist:.6f}\n")
            f.write("\n")
    print(f"✅ Distances saved to: {output_file}")


def main():
    """Compute distances for all ANN methods."""
    
    # Paths
    base_dir = Path('/home/marialtr/project_part3/Part3')
    embeddings_file = base_dir / 'output/embeddings/vectors_50k_opt.dat'
    ids_file = base_dir / 'output/embeddings/vectors_50k_opt_ids.txt'
    query_embeddings_file = base_dir / 'output/embeddings/query'  # Note: no .dat extension
    query_ids_file = base_dir / 'output/embeddings/query_ids.txt'
    search_dir = base_dir / 'output/search'
    output_dir = base_dir / 'output/evaluation'
    output_dir.mkdir(exist_ok=True)
    
    # Check if files exist
    if not embeddings_file.exists():
        print(f"❌ Error: Embeddings file not found: {embeddings_file}")
        sys.exit(1)
    
    if not ids_file.exists():
        print(f"❌ Error: IDs file not found: {ids_file}")
        sys.exit(1)
    
    if not query_embeddings_file.exists():
        print(f"❌ Error: Query embeddings file not found: {query_embeddings_file}")
        sys.exit(1)
    
    # Methods to process
    methods = {
        'LSH': 'results_lsh.txt',
        'Hypercube': 'results_hypercube.txt',
        'IVF-Flat': 'results_ivfflat.txt',
        'IVF-PQ': 'results_ivfpq.txt',
        'Neural LSH': 'results_nlsh.txt'
    }
    
    distance_type = 'cosine'  # or 'l2'
    print(f"\n🔍 Computing {distance_type.upper()} distances for all methods...")
    
    # Load dataset embeddings once (50k proteins)
    print("\nLoading dataset embeddings (50k proteins)...")
    dataset_embeddings = read_embeddings_memmap(embeddings_file, ids_file)
    print(f"Loaded {len(dataset_embeddings)} dataset embeddings")
    
    # Load query embeddings
    print("\nLoading query embeddings...")
    query_embeddings = read_embeddings_memmap(query_embeddings_file, query_ids_file)
    print(f"Loaded {len(query_embeddings)} query embeddings")
    
    # Combine both dictionaries (queries + dataset)
    all_embeddings = {**dataset_embeddings, **query_embeddings}
    print(f"Total embeddings available: {len(all_embeddings)}")
    
    # Process each method
    all_distances = {}
    
    for method_name, results_filename in methods.items():
        results_file = search_dir / results_filename
        
        if not results_file.exists():
            print(f"⚠️  Warning: Results file not found: {results_file}")
            continue
        
        distances = compute_distances_for_method_with_embeddings(
            method_name, 
            results_file, 
            all_embeddings,
            distance_type
        )
        
        all_distances[method_name] = distances
        
        # Save individual method distances
        output_file = output_dir / f'distances_{results_filename}'
        save_distances(distances, output_file)
    
    print(f"\n{'='*80}")
    print(f"✅ Distance computation complete!")
    print(f"{'='*80}")
    
    # Print summary statistics
    print("\nDistance Statistics:")
    print("-" * 80)
    for method_name, distances in all_distances.items():
        all_dists = [d for query_dists in distances.values() for _, d in query_dists if d != float('inf')]
        if all_dists:
            print(f"{method_name:20} | Mean: {np.mean(all_dists):.4f} | "
                  f"Std: {np.std(all_dists):.4f} | "
                  f"Min: {np.min(all_dists):.4f} | "
                  f"Max: {np.max(all_dists):.4f}")


if __name__ == '__main__':
    main()
