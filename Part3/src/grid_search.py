#!/usr/bin/env python3
"""
Grid search for ANN hyperparameter tuning.
Runs all method/parameter combinations and saves results to CSV.
"""

import os
import sys
import csv
import argparse
from itertools import product
from typing import Dict, List, Tuple, Optional

# Local imports
sys.path.append(os.path.dirname(__file__))
from protein_search import (
	run_protein_search,
	compute_recall,
	parse_blast_tsv,
	parse_neighbor_results,
)


def get_lsh_grid():
	"""Generate LSH parameter grid: k, L, w"""
	k_vals = [2, 4, 6]
	L_vals = [5, 10, 15]
	w_vals = [20, 40, 80, 120, 300, 500, 1000]
	
	for k, L, w in product(k_vals, L_vals, w_vals):
		yield {
			"k": k,
			"L": L,
			"w": w,
		}


def get_hypercube_grid():
	"""Generate Hypercube parameter grid: kproj, w, M, probes"""
	kproj_vals = [12, 14, 16, 20]
	w_vals = [20, 40, 80, 120, 300, 500, 1000]
	M_vals = [2000, 5000, 10000]
	probes_vals = [100, 250, 500]
	
	for kproj, w, M, probes in product(kproj_vals, w_vals, M_vals, probes_vals):
		yield {
			"kproj": kproj,
			"w": w,
			"M": M,
			"probes": probes,
		}


def get_ivfflat_grid():
	"""Generate IVF-Flat parameter grid: kclusters, nprobe"""
	kclusters_vals = [200, 500, 1000, 5000]
	nprobe_vals = [50, 100, 250, 500, 1500]
	
	for kclusters, nprobe in product(kclusters_vals, nprobe_vals):
		# Only yield if nprobe < kclusters
		if nprobe < kclusters:
			yield {
				"kclusters": kclusters,
				"nprobe": nprobe,
			}


def get_ivfpq_grid():
	"""Generate IVF-PQ parameter grid: kclusters, nprobe, M (subvectors)"""
	kclusters_vals = [200, 500, 1000, 5000]
	nprobe_vals = [50, 100, 250, 500, 1500]
	M_vals = [8, 16]
	
	for kclusters, nprobe, M in product(kclusters_vals, nprobe_vals, M_vals):
		# Only yield if nprobe < kclusters
		if nprobe < kclusters:
			yield {
				"kclusters": kclusters,
				"nprobe": nprobe,
				"ivfpq_M": M,
			}


def get_nlsh_grid():
	"""Generate NLSH parameter grid: T, m, layers, nodes"""
	T_vals = [1000, 1500]
	m_vals = [1800, 2000, 2200]
	layers_vals = [5, 10, 15]
	nodes_vals = [128, 256, 512]
	
	for T, m, layers, nodes in product(T_vals, m_vals, layers_vals, nodes_vals):
		yield {
			"nlsh_T": T,
			"nlsh_m": m,
			"nlsh_layers": layers,
			"nlsh_nodes": nodes,
		}


def run_grid_search(
	base_dat: str,
	query_fasta: str,
	output_dir: str,
	method: str = "all",
	seed: int = 42,
	nbits: int = 8,
	nlsh_epochs: int = 8,
	nlsh_batch_size: int = 512,
	nlsh_lr: float = 1e-3,
):
	"""
	Run grid search for specified method(s).
	
	Args:
		base_dat: Path to base protein vectors .dat
		query_fasta: Path to query FASTA
		output_dir: Directory to save results and CSVs
		method: "all" or specific method name
		seed: Random seed
		nbits: Bits per subspace (IVF-PQ)
		nlsh_epochs: Training epochs (NLSH)
		nlsh_batch_size: Batch size (NLSH)
		nlsh_lr: Learning rate (NLSH)
	"""
	
	os.makedirs(output_dir, exist_ok=True)
	
	# BLAST reference results
	blast_results_path = "output/blast/topN"
	
	N_vals = [1, 10, 50]
	seed_val = seed
	
	# Dictionary to store results per method
	all_results = {
		"lsh": [],
		"hypercube": [],
		"ivfflat": [],
		"ivfpq": [],
		"nlsh": [],
	}
	
	methods_to_run = [method] if method != "all" else ["lsh", "hypercube", "ivfflat", "ivfpq", "nlsh"]
	
	total_runs = sum(
		len(list(N_vals)) * len(list(get_grid_func()))
		for get_grid_func in [get_lsh_grid, get_hypercube_grid, get_ivfflat_grid, get_ivfpq_grid, get_nlsh_grid]
		if (methods_to_run == ["all"]) or (
			(get_grid_func == get_lsh_grid and "lsh" in methods_to_run) or
			(get_grid_func == get_hypercube_grid and "hypercube" in methods_to_run) or
			(get_grid_func == get_ivfflat_grid and "ivfflat" in methods_to_run) or
			(get_grid_func == get_ivfpq_grid and "ivfpq" in methods_to_run) or
			(get_grid_func == get_nlsh_grid and "nlsh" in methods_to_run)
		)
	)
	
	run_count = 0
	
	# LSH grid search
	if "lsh" in methods_to_run:
		print(f"\n{'='*80}")
		print("LSH GRID SEARCH")
		print(f"{'='*80}")
		
		for N in N_vals:
			for param_set in get_lsh_grid():
				run_count += 1
				param_str = f"N{N}_k{param_set['k']}_L{param_set['L']}_w{int(param_set['w'])}"
				output_txt = os.path.join(output_dir, f"lsh_{param_str}.txt")
				
				print(f"\n[{run_count}/{total_runs}] LSH: N={N}, k={param_set['k']}, L={param_set['L']}, w={param_set['w']}")
				
				try:
					qps = run_protein_search(
						base_dat=base_dat,
						query_fasta=query_fasta,
						output_txt=output_txt,
						method="lsh",
						N=N,
						seed=seed_val,
						k=param_set['k'],
						L=param_set['L'],
						w=param_set['w'],
					)
					
					# Compute recall
					blast_tsv = os.path.join(blast_results_path, f"blast_results_top{N}.tsv")
					if os.path.exists(blast_tsv) and os.path.exists(output_txt):
						mean_recall, _ = compute_recall(blast_tsv, output_txt, N)
						
						result = {
							"N": N,
							"seed": seed_val,
							"k": param_set['k'],
							"L": param_set['L'],
							"w": param_set['w'],
							"recall": mean_recall,
							"qps": qps if qps else 0.0,
							"time_per_query": 1.0/qps if qps and qps > 0 else float('inf'),
						}
						all_results["lsh"].append(result)
						print(f"  Recall@{N}: {mean_recall:.4f}, QPS: {qps:.2f if qps else 0}")
					
					# Clean up
					if os.path.exists(output_txt):
						os.remove(output_txt)
					query_dat = output_txt.replace(".txt", ".queries.dat")
					query_ids = output_txt.replace(".txt", ".queries_ids.txt")
					if os.path.exists(query_dat):
						os.remove(query_dat)
					if os.path.exists(query_ids):
						os.remove(query_ids)
					
				except Exception as e:
					print(f"  ERROR: {e}")
					continue
	
	# Hypercube grid search
	if "hypercube" in methods_to_run:
		print(f"\n{'='*80}")
		print("HYPERCUBE GRID SEARCH")
		print(f"{'='*80}")
		
		for N in N_vals:
			for param_set in get_hypercube_grid():
				run_count += 1
				param_str = f"N{N}_kproj{param_set['kproj']}_w{int(param_set['w'])}_M{param_set['M']}_probes{param_set['probes']}"
				output_txt = os.path.join(output_dir, f"hypercube_{param_str}.txt")
				
				print(f"\n[{run_count}/{total_runs}] Hypercube: N={N}, kproj={param_set['kproj']}, w={param_set['w']}, M={param_set['M']}, probes={param_set['probes']}")
				
				try:
					qps = run_protein_search(
						base_dat=base_dat,
						query_fasta=query_fasta,
						output_txt=output_txt,
						method="hypercube",
						N=N,
						seed=seed_val,
						kproj=param_set['kproj'],
						w=param_set['w'],
						M=param_set['M'],
						probes=param_set['probes'],
					)
					
					# Compute recall
					blast_tsv = os.path.join(blast_results_path, f"blast_results_top{N}.tsv")
					if os.path.exists(blast_tsv) and os.path.exists(output_txt):
						mean_recall, _ = compute_recall(blast_tsv, output_txt, N)
						
						result = {
							"N": N,
							"seed": seed_val,
							"kproj": param_set['kproj'],
							"w": param_set['w'],
							"M": param_set['M'],
							"probes": param_set['probes'],
							"recall": mean_recall,
							"qps": qps if qps else 0.0,
							"time_per_query": 1.0/qps if qps and qps > 0 else float('inf'),
						}
						all_results["hypercube"].append(result)
						print(f"  Recall@{N}: {mean_recall:.4f}, QPS: {qps:.2f if qps else 0}")
					
					# Clean up
					if os.path.exists(output_txt):
						os.remove(output_txt)
					query_dat = output_txt.replace(".txt", ".queries.dat")
					query_ids = output_txt.replace(".txt", ".queries_ids.txt")
					if os.path.exists(query_dat):
						os.remove(query_dat)
					if os.path.exists(query_ids):
						os.remove(query_ids)
					
				except Exception as e:
					print(f"  ERROR: {e}")
					continue
	
	# IVF-Flat grid search
	if "ivfflat" in methods_to_run:
		print(f"\n{'='*80}")
		print("IVF-FLAT GRID SEARCH")
		print(f"{'='*80}")
		
		for N in N_vals:
			for param_set in get_ivfflat_grid():
				run_count += 1
				param_str = f"N{N}_kclusters{param_set['kclusters']}_nprobe{param_set['nprobe']}"
				output_txt = os.path.join(output_dir, f"ivfflat_{param_str}.txt")
				
				print(f"\n[{run_count}/{total_runs}] IVF-Flat: N={N}, kclusters={param_set['kclusters']}, nprobe={param_set['nprobe']}")
				
				try:
					qps = run_protein_search(
						base_dat=base_dat,
						query_fasta=query_fasta,
						output_txt=output_txt,
						method="ivfflat",
						N=N,
						seed=seed_val,
						kclusters=param_set['kclusters'],
						nprobe=param_set['nprobe'],
					)
					
					# Compute recall
					blast_tsv = os.path.join(blast_results_path, f"blast_results_top{N}.tsv")
					if os.path.exists(blast_tsv) and os.path.exists(output_txt):
						mean_recall, _ = compute_recall(blast_tsv, output_txt, N)
						
						result = {
							"N": N,
							"seed": seed_val,
							"kclusters": param_set['kclusters'],
							"nprobe": param_set['nprobe'],
							"recall": mean_recall,
							"qps": qps if qps else 0.0,
							"time_per_query": 1.0/qps if qps and qps > 0 else float('inf'),
						}
						all_results["ivfflat"].append(result)
						print(f"  Recall@{N}: {mean_recall:.4f}, QPS: {qps:.2f if qps else 0}")
					
					# Clean up
					if os.path.exists(output_txt):
						os.remove(output_txt)
					query_dat = output_txt.replace(".txt", ".queries.dat")
					query_ids = output_txt.replace(".txt", ".queries_ids.txt")
					if os.path.exists(query_dat):
						os.remove(query_dat)
					if os.path.exists(query_ids):
						os.remove(query_ids)
					
				except Exception as e:
					print(f"  ERROR: {e}")
					continue
	
	# IVF-PQ grid search
	if "ivfpq" in methods_to_run:
		print(f"\n{'='*80}")
		print("IVF-PQ GRID SEARCH")
		print(f"{'='*80}")
		
		for N in N_vals:
			for param_set in get_ivfpq_grid():
				run_count += 1
				param_str = f"N{N}_kclusters{param_set['kclusters']}_nprobe{param_set['nprobe']}_M{param_set['ivfpq_M']}"
				output_txt = os.path.join(output_dir, f"ivfpq_{param_str}.txt")
				
				print(f"\n[{run_count}/{total_runs}] IVF-PQ: N={N}, kclusters={param_set['kclusters']}, nprobe={param_set['nprobe']}, M={param_set['ivfpq_M']}")
				
				try:
					qps = run_protein_search(
						base_dat=base_dat,
						query_fasta=query_fasta,
						output_txt=output_txt,
						method="ivfpq",
						N=N,
						seed=seed_val,
						kclusters=param_set['kclusters'],
						nprobe=param_set['nprobe'],
						nbits=nbits,
						ivfpq_M=param_set['ivfpq_M'],
					)
					
					# Compute recall
					blast_tsv = os.path.join(blast_results_path, f"blast_results_top{N}.tsv")
					if os.path.exists(blast_tsv) and os.path.exists(output_txt):
						mean_recall, _ = compute_recall(blast_tsv, output_txt, N)
						
						result = {
							"N": N,
							"seed": seed_val,
							"kclusters": param_set['kclusters'],
							"nprobe": param_set['nprobe'],
							"ivfpq_M": param_set['ivfpq_M'],
							"nbits": nbits,
							"recall": mean_recall,
							"qps": qps if qps else 0.0,
							"time_per_query": 1.0/qps if qps and qps > 0 else float('inf'),
						}
						all_results["ivfpq"].append(result)
						print(f"  Recall@{N}: {mean_recall:.4f}, QPS: {qps:.2f if qps else 0}")
					
					# Clean up
					if os.path.exists(output_txt):
						os.remove(output_txt)
					query_dat = output_txt.replace(".txt", ".queries.dat")
					query_ids = output_txt.replace(".txt", ".queries_ids.txt")
					if os.path.exists(query_dat):
						os.remove(query_dat)
					if os.path.exists(query_ids):
						os.remove(query_ids)
					
				except Exception as e:
					print(f"  ERROR: {e}")
					continue
	
	# NLSH grid search
	if "nlsh" in methods_to_run:
		print(f"\n{'='*80}")
		print("NLSH GRID SEARCH")
		print(f"{'='*80}")
		
		for N in N_vals:
			for param_set in get_nlsh_grid():
				run_count += 1
				param_str = f"N{N}_T{param_set['nlsh_T']}_m{param_set['nlsh_m']}_layers{param_set['nlsh_layers']}_nodes{param_set['nlsh_nodes']}"
				output_txt = os.path.join(output_dir, f"nlsh_{param_str}.txt")
				
				print(f"\n[{run_count}/{total_runs}] NLSH: N={N}, T={param_set['nlsh_T']}, m={param_set['nlsh_m']}, layers={param_set['nlsh_layers']}, nodes={param_set['nlsh_nodes']}")
				
				try:
					qps = run_protein_search(
						base_dat=base_dat,
						query_fasta=query_fasta,
						output_txt=output_txt,
						method="nlsh",
						N=N,
						seed=seed_val,
						nlsh_T=param_set['nlsh_T'],
						nlsh_m=param_set['nlsh_m'],
						nlsh_layers=param_set['nlsh_layers'],
						nlsh_nodes=param_set['nlsh_nodes'],
						nlsh_epochs=nlsh_epochs,
						nlsh_batch_size=nlsh_batch_size,
						nlsh_lr=nlsh_lr,
					)
					
					# Compute recall
					blast_tsv = os.path.join(blast_results_path, f"blast_results_top{N}.tsv")
					if os.path.exists(blast_tsv) and os.path.exists(output_txt):
						mean_recall, _ = compute_recall(blast_tsv, output_txt, N)
						
						result = {
							"N": N,
							"seed": seed_val,
							"nlsh_T": param_set['nlsh_T'],
							"nlsh_m": param_set['nlsh_m'],
							"nlsh_layers": param_set['nlsh_layers'],
							"nlsh_nodes": param_set['nlsh_nodes'],
							"nlsh_epochs": nlsh_epochs,
							"nlsh_batch_size": nlsh_batch_size,
							"nlsh_lr": nlsh_lr,
							"recall": mean_recall,
							"qps": qps if qps else 0.0,
							"time_per_query": 1.0/qps if qps and qps > 0 else float('inf'),
						}
						all_results["nlsh"].append(result)
						print(f"  Recall@{N}: {mean_recall:.4f}, QPS: {qps:.2f if qps else 0}")
					
					# Clean up
					if os.path.exists(output_txt):
						os.remove(output_txt)
					query_dat = output_txt.replace(".txt", ".queries.dat")
					query_ids = output_txt.replace(".txt", ".queries_ids.txt")
					if os.path.exists(query_dat):
						os.remove(query_dat)
					if os.path.exists(query_ids):
						os.remove(query_ids)
					
				except Exception as e:
					print(f"  ERROR: {e}")
					continue
	
	# Save results to CSV files
	print(f"\n{'='*80}")
	print("SAVING RESULTS TO CSV")
	print(f"{'='*80}")
	
	for method, results in all_results.items():
		if results:
			csv_path = os.path.join(output_dir, f"grid_search_{method}.csv")
			
			# Get fieldnames from first result
			fieldnames = list(results[0].keys())
			
			with open(csv_path, "w", newline="") as f:
				writer = csv.DictWriter(f, fieldnames=fieldnames)
				writer.writeheader()
				writer.writerows(results)
			
			print(f"Saved {len(results)} results to {csv_path}")


def main():
	parser = argparse.ArgumentParser("Grid search for ANN hyperparameter tuning")
	parser.add_argument("-d", required=True, help="Path to base protein vectors .dat")
	parser.add_argument("-q", required=True, help="Path to query FASTA")
	parser.add_argument("--output-dir", default="output/grid_search", help="Output directory for results")
	parser.add_argument("--method", default="all", choices=["lsh", "hypercube", "ivfflat", "ivfpq", "nlsh", "all"],
						help="Method to grid search")
	parser.add_argument("--seed", type=int, default=42, help="Random seed")
	parser.add_argument("--nbits", type=int, default=8, help="Bits per subspace (IVF-PQ)")
	parser.add_argument("--nlsh-epochs", type=int, default=8, help="NLSH training epochs")
	parser.add_argument("--nlsh-batch-size", type=int, default=512, help="NLSH batch size")
	parser.add_argument("--nlsh-lr", type=float, default=1e-3, help="NLSH learning rate")
	
	args = parser.parse_args()
	
	run_grid_search(
		base_dat=args.d,
		query_fasta=args.q,
		output_dir=args.output_dir,
		method=args.method.lower(),
		seed=args.seed,
		nbits=args.nbits,
		nlsh_epochs=args.nlsh_epochs,
		nlsh_batch_size=args.nlsh_batch_size,
		nlsh_lr=args.nlsh_lr,
	)


if __name__ == "__main__":
	main()
