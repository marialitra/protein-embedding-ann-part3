#!/bin/bash
# Quick smoke test for protein search with all algorithms

set -e

PROJ_ROOT="/home/marialtr/project_part3"
SEARCH_BIN="${PROJ_ROOT}/Algorithms/AlgorithmsPart1/search"
BASE_DAT="${PROJ_ROOT}/Part3/output/vectors_50k.dat"
QUERY_DAT="${PROJ_ROOT}/Part3/output/protein_ivf_neighbors.queries.dat"
OUTPUT_DIR="${PROJ_ROOT}/Part3/output"

echo "=== Protein Search Smoke Test ==="
echo "Testing all algorithms with cosine distance on protein data"
echo ""

# Test IVFFlat (already validated)
echo "[1/4] Testing IVFFlat..."
$SEARCH_BIN \
  -d "$BASE_DAT" \
  -q "$QUERY_DAT" \
  -kclusters 128 \
  -nprobe 5 \
  -o "${OUTPUT_DIR}/test_ivfflat.txt" \
  -N 5 \
  -type protein \
  -range false \
  -ivfflat \
  -seed 42
echo "✓ IVFFlat completed"

# Test LSH
echo "[2/4] Testing LSH..."
$SEARCH_BIN \
  -d "$BASE_DAT" \
  -q "$QUERY_DAT" \
  -k 4 \
  -L 5 \
  -w 4.0 \
  -o "${OUTPUT_DIR}/test_lsh.txt" \
  -N 5 \
  -type protein \
  -range false \
  -lsh \
  -seed 42
echo "✓ LSH completed"

# Test Hypercube
echo "[3/4] Testing Hypercube..."
$SEARCH_BIN \
  -d "$BASE_DAT" \
  -q "$QUERY_DAT" \
  -kproj 12 \
  -w 4.0 \
  -M 1000 \
  -probes 10 \
  -o "${OUTPUT_DIR}/test_hypercube.txt" \
  -N 5 \
  -type protein \
  -range false \
  -hypercube \
  -seed 42
echo "✓ Hypercube completed"

# Test IVFPQ
echo "[4/4] Testing IVFPQ..."
$SEARCH_BIN \
  -d "$BASE_DAT" \
  -q "$QUERY_DAT" \
  -kclusters 64 \
  -nprobe 5 \
  -M 16 \
  -nbits 8 \
  -o "${OUTPUT_DIR}/test_ivfpq.txt" \
  -N 5 \
  -type protein \
  -range false \
  -ivfpq \
  -seed 42
echo "✓ IVFPQ completed"

echo ""
echo "=== All tests passed! ==="
echo "Results saved to ${OUTPUT_DIR}/test_*.txt"
