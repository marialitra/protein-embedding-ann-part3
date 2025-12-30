#!/usr/bin/env python3
"""
Step 3: Experimental Comparison & Biological Evaluation
Quantitative comparison of ANN methods + functional homolog analysis
"""

import os
import sys
import csv
from collections import defaultdict
from urllib.request import urlopen
import time

sys.path.append(os.path.dirname(__file__))
from protein_search import compute_recall, parse_blast_tsv, parse_ann_txt


def extract_protein_info_from_fasta(fasta_file):
    """Extract protein IDs from FASTA file"""
    proteins = []
    with open(fasta_file, 'r') as f:
        for line in f:
            if line.startswith('>'):
                # Extract ID from header
                parts = line.strip()[1:].split()
                protein_id = parts[0]
                proteins.append(protein_id)
    return proteins


def get_ann_results(method, results_file, topN=5):
    """Parse ANN results file and return dict of {query: [neighbors]}"""
    results = defaultdict(list)
    current_query = None
    
    with open(results_file, 'r') as f:
        for line in f:
            line = line.strip()
            if line.startswith('Query:'):
                current_query = line.split('Query:')[1].strip()
            elif line.startswith('Nearest neighbor') and current_query:
                try:
                    neighbor_id = line.split(':')[1].strip()
                    if len(results[current_query]) < topN:
                        results[current_query].append(neighbor_id)
                except:
                    pass
    
    return results


def fetch_uniprot_info(protein_id):
    """Fetch protein information from UniProt API"""
    try:
        # Try to get UniProt ID from NCBI format (sp|ID|...)
        if '|' in protein_id:
            parts = protein_id.split('|')
            if len(parts) >= 2:
                uniprot_id = parts[1]
            else:
                uniprot_id = protein_id
        else:
            uniprot_id = protein_id
        
        url = f"https://rest.uniprot.org/uniprotkb/{uniprot_id}.json"
        response = urlopen(url, timeout=5)
        data = response.read().decode('utf-8')
        
        import json
        info = json.loads(data)
        
        # Extract key information
        result = {
            'id': uniprot_id,
            'name': info.get('uniProtkbId', ''),
            'protein_name': '',
            'organism': '',
            'function': '',
            'ec_number': '',
            'domains': [],
            'go_terms': [],
        }
        
        # Protein name
        if 'proteinDescription' in info:
            if 'recommendedName' in info['proteinDescription']:
                result['protein_name'] = info['proteinDescription']['recommendedName'].get('fullName', {}).get('value', '')
        
        # Organism
        if 'organism' in info:
            result['organism'] = info['organism'].get('scientificName', '')
        
        # Function from comments
        if 'comments' in info:
            for comment in info['comments']:
                if comment.get('commentType') == 'FUNCTION':
                    result['function'] = comment.get('texts', [{}])[0].get('value', '')
        
        # EC numbers
        if 'proteinDescription' in info:
            prot_desc = info['proteinDescription']
            if 'ecNumbers' in prot_desc:
                result['ec_number'] = ', '.join([ec.get('value', '') for ec in prot_desc['ecNumbers']])
        
        # Pfam domains
        if 'features' in info:
            for feature in info['features']:
                if feature.get('type') == 'Domain':
                    result['domains'].append(feature.get('description', ''))
        
        # GO terms
        if 'uniProtkbCrossReferences' in info:
            for xref in info['uniProtkbCrossReferences']:
                if xref.get('database') == 'GO':
                    go_id = xref.get('id', '')
                    go_props = xref.get('properties', [])
                    go_desc = ''
                    for prop in go_props:
                        if prop.get('key') == 'GoTerm':
                            go_desc = prop.get('value', '')
                    if go_desc:
                        result['go_terms'].append(f"{go_id}: {go_desc}")
        
        return result
    except Exception as e:
        return {
            'id': protein_id,
            'error': str(e),
            'protein_name': 'N/A',
            'organism': 'N/A',
            'function': 'N/A'
        }


def analyze_query_homologs(query_id, blast_results_dict, ann_results_dict, output_dir, N=5):
    """
    Analyze a query protein and find potential remote homologs
    - Low BLAST identity (<30%) but high embedding similarity
    """
    
    results = {
        'query_id': query_id,
        'candidates': []
    }
    
    # Get BLAST results for this query
    blast_hits = set()
    blast_identities = {}
    
    if query_id in blast_results_dict:
        for hit in blast_results_dict[query_id][:N]:
            hit_id = hit
            blast_hits.add(hit_id)
            # Extract identity from BLAST results (would need full BLAST parsing)
            # For now, mark as BLAST hit
            blast_identities[hit_id] = 'BLAST_HIT'
    
    # Get ANN results for this query
    for method, ann_results in ann_results_dict.items():
        if query_id not in ann_results:
            continue
        
        for rank, neighbor_id in enumerate(ann_results[query_id][:N], 1):
            # Check if this is NOT in BLAST top hits (potential remote homolog)
            if neighbor_id not in blast_hits:
                # Fetch UniProt info for both query and neighbor
                query_info = fetch_uniprot_info(query_id)
                neighbor_info = fetch_uniprot_info(neighbor_id)
                
                results['candidates'].append({
                    'method': method,
                    'rank': rank,
                    'neighbor_id': neighbor_id,
                    'neighbor_info': neighbor_info,
                    'query_info': query_info,
                    'in_blast_hits': neighbor_id in blast_hits,
                })
    
    return results


def quantitative_comparison(methods, blast_results_file, results_dir, N=5):
    """Quantitative comparison of all methods"""
    
    print("\n" + "="*80)
    print("QUANTITATIVE COMPARISON - ALL METHODS")
    print("="*80)
    
    comparison_data = {}
    
    # Load BLAST ground truth
    blast_gt = parse_blast_tsv(blast_results_file, N)
    
    for method in methods:
        results_file = os.path.join(results_dir, f"results_{method}.txt")
        
        if not os.path.exists(results_file):
            print(f"  [WARNING] File not found: {results_file}")
            continue
        
        # Compute recall
        recall, per_query = compute_recall(blast_results_file, results_file, N)
        
        comparison_data[method] = {
            'recall': recall,
            'recall_percent': recall * 100,
            'per_query': per_query
        }
        
        print(f"\n{method.upper()}")
        print(f"  Recall@{N}: {recall:.4f} ({recall*100:.2f}%)")
        print(f"  Per-query stats:")
        
        if per_query:
            recalls = list(per_query.values())
            print(f"    - Min: {min(recalls):.4f}")
            print(f"    - Max: {max(recalls):.4f}")
            print(f"    - Avg: {sum(recalls)/len(recalls):.4f}")
            print(f"    - Median: {sorted(recalls)[len(recalls)//2]:.4f}")
    
    return comparison_data


def biological_evaluation(query_fasta, blast_results_file, results_dir, methods, output_file):
    """Biological evaluation of remote homologs"""
    
    print("\n" + "="*80)
    print("BIOLOGICAL EVALUATION - REMOTE HOMOLOG ANALYSIS")
    print("="*80)
    
    # Load BLAST ground truth
    blast_gt = parse_blast_tsv(blast_results_file, topN=5)
    
    # Load ANN results for all methods
    ann_results = {}
    for method in methods:
        results_file = os.path.join(results_dir, f"results_{method}.txt")
        if os.path.exists(results_file):
            ann_results[method] = get_ann_results(method, results_file, topN=5)
    
    # Get list of queries
    queries = extract_protein_info_from_fasta(query_fasta)
    
    # Focus on top queries (by recall potential)
    selected_queries = queries[:5]  # Analyze first 5 queries as examples
    
    print(f"\nAnalyzing {len(selected_queries)} representative queries...")
    print(f"Methods: {', '.join(methods)}\n")
    
    # Open output report file
    with open(output_file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([
            'Query_ID', 'Method', 'Neighbor_ID', 'Rank',
            'In_BLAST_Hits', 'Neighbor_Name', 'Organism',
            'Function', 'EC_Number', 'Domains', 'GO_Terms'
        ])
        
        for query_id in selected_queries:
            print(f"\n{'='*80}")
            print(f"Query: {query_id}")
            print(f"{'='*80}")
            
            # Get BLAST hits
            blast_hits = blast_gt.get(query_id, set())
            print(f"BLAST Top hits: {', '.join(list(blast_hits)[:3])}...")
            
            # For each method
            for method in methods:
                if method not in ann_results or query_id not in ann_results[method]:
                    continue
                
                print(f"\n  {method.upper()} Results:")
                neighbors = ann_results[method][query_id]
                
                for rank, neighbor_id in enumerate(neighbors, 1):
                    in_blast = neighbor_id in blast_hits
                    status = "✓ BLAST HIT" if in_blast else "⚠ NOVEL"
                    
                    # Fetch protein info
                    try:
                        neighbor_info = fetch_uniprot_info(neighbor_id)
                        
                        protein_name = neighbor_info.get('protein_name', 'N/A')[:50]
                        organism = neighbor_info.get('organism', 'N/A')[:30]
                        function = neighbor_info.get('function', 'N/A')[:50]
                        
                        print(f"    [{rank}] {neighbor_id:15s} {status}")
                        print(f"        Name: {protein_name}")
                        print(f"        Organism: {organism}")
                        if function:
                            print(f"        Function: {function}")
                        
                        # Write to CSV
                        writer.writerow([
                            query_id,
                            method,
                            neighbor_id,
                            rank,
                            'Yes' if in_blast else 'No',
                            protein_name,
                            organism,
                            function,
                            neighbor_info.get('ec_number', ''),
                            '; '.join(neighbor_info.get('domains', [])),
                            '; '.join(neighbor_info.get('go_terms', [])[:2])  # First 2 GO terms
                        ])
                    except Exception as e:
                        print(f"    [{rank}] {neighbor_id:15s} {status} [ERROR: {e}]")
                        writer.writerow([query_id, method, neighbor_id, rank, 'Yes' if in_blast else 'No', str(e)])
    
    print(f"\n{'='*80}")
    print(f"Biological evaluation report saved to: {output_file}")
    print(f"{'='*80}")


def main():
    # Configuration
    QUERY_FASTA = "Data/targets.fasta"
    BLAST_RESULTS = "output/blast/topN/blast_results_top5.tsv"
    RESULTS_DIR = "output/search"
    METHODS = ['lsh', 'hypercube', 'ivfflat', 'ivfpq', 'nlsh']
    OUTPUT_DIR = "output/evaluation"
    N = 5
    
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    print("\n" + "="*80)
    print("STEP 3: EXPERIMENTAL COMPARISON & BIOLOGICAL EVALUATION")
    print("="*80)
    
    # Part 1: Quantitative comparison
    comparison_data = quantitative_comparison(METHODS, BLAST_RESULTS, RESULTS_DIR, N)
    
    # Save comparison to CSV
    comparison_csv = os.path.join(OUTPUT_DIR, "quantitative_comparison.csv")
    with open(comparison_csv, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['Method', 'Recall', 'Recall_Percent'])
        writer.writeheader()
        for method, data in comparison_data.items():
            writer.writerow({
                'Method': method,
                'Recall': data['recall'],
                'Recall_Percent': data['recall_percent']
            })
    
    print(f"\nQuantitative comparison saved to: {comparison_csv}")
    
    # Part 2: Biological evaluation
    report_file = os.path.join(OUTPUT_DIR, "biological_evaluation.csv")
    biological_evaluation(QUERY_FASTA, BLAST_RESULTS, RESULTS_DIR, METHODS, report_file)
    
    print("\n" + "="*80)
    print("EVALUATION COMPLETE")
    print("="*80)
    print(f"Results saved to: {OUTPUT_DIR}/")


if __name__ == "__main__":
    main()
