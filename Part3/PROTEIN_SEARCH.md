# Protein Vector Search with Cosine Distance

This integration adds support for searching protein embeddings (320-D vectors) using cosine similarity across all four algorithms: LSH, Hypercube, IVFFlat, and IVFPQ.

## Quick Start

### 1. Generate Protein Embeddings

```bash
# Create embeddings from FASTA file
python3 Part3/src/protein_embed.py \
  -i Part3/Data/swissprot_50k.fasta \
  -o Part3/output/vectors_50k.dat \
  --batch-size 64
```

### 2. Search Using Python Wrapper (IVFFlat)

```bash
python3 Part3/src/protein_search.py \
  --base-dat Part3/output/vectors_50k.dat \
  --query-fasta Part3/Data/targets.fasta \
  -o Part3/output/neighbors.txt \
  --kclusters 1024 \
  --nprobe 10 \
  -N 10 \
  --seed 42
```

The wrapper automatically:
- Generates query embeddings from FASTA
- Builds the C executable if needed
- Runs IVFFlat with `-type protein` (cosine distance)

### 3. Direct C Binary Usage

All algorithms support `-type protein` which automatically enables cosine distance:

#### IVFFlat
```bash
./Algorithms/AlgorithmsPart1/search \
  -d Part3/output/vectors_50k.dat \
  -q Part3/output/queries.dat \
  -kclusters 1024 -nprobe 10 \
  -o output.txt -N 10 \
  -type protein -range false -ivfflat -seed 42
```

#### LSH
```bash
./Algorithms/AlgorithmsPart1/search \
  -d Part3/output/vectors_50k.dat \
  -q Part3/output/queries.dat \
  -k 4 -L 5 -w 4.0 \
  -o output.txt -N 10 \
  -type protein -range false -lsh -seed 42
```

#### Hypercube
```bash
./Algorithms/AlgorithmsPart1/search \
  -d Part3/output/vectors_50k.dat \
  -q Part3/output/queries.dat \
  -kproj 12 -w 4.0 -M 5000 -probes 10 \
  -o output.txt -N 10 \
  -type protein -range false -hypercube -seed 42
```

#### IVFPQ
```bash
./Algorithms/AlgorithmsPart1/search \
  -d Part3/output/vectors_50k.dat \
  -q Part3/output/queries.dat \
  -kclusters 256 -nprobe 10 -M 16 -nbits 8 \
  -o output.txt -N 10 \
  -type protein -range false -ivfpq -seed 42
```

## Data Format

### Input Files
- **Base/Query `.dat`**: Float32 binary matrix, row-major layout
  - Pure format: N × 320 floats
  - With IDs: N × (320 + 50) floats (last 50 slots for ASCII IDs, auto-detected and stripped)

### Output Format
```
IVFFlat

Query: 0
Nearest neighbor-1: 42
Nearest neighbor-2: 1337
...

Query: 1
Nearest neighbor-1: 999
...
```

## Cosine Distance

When `-type protein` is specified:
- **Metric**: 1 − cos(a, b) ∈ [0, 2]
- **IVFFlat**: Spherical k-means (normalized centroids)
- **LSH/Hypercube/IVFPQ**: Direct cosine distance in candidate scoring

For MNIST/SIFT, Euclidean distance is used as before.

## Performance Tuning

### IVFFlat (Recommended for proteins)
- `kclusters`: 256–2048 (more clusters = better recall, slower indexing)
- `nprobe`: 5–20 (more probes = better recall, slower search)
- Trade-off: Use `kclusters=1024, nprobe=10` for balanced speed/accuracy

### LSH
- `k=4, L=10, w=4.0`: Good starting point
- Increase `L` for better recall

### Hypercube
- `kproj=12–14, M=5000, probes=10`: Balanced
- Higher `M` and `probes` improve recall

### IVFPQ
- `M=16, nbits=8`: Standard compression (16× size reduction)
- Trade memory vs accuracy by adjusting `M` and `nbits`

## Testing

Run smoke test across all algorithms:
```bash
bash Part3/test_protein_search.sh
```

## Technical Details

### Implementation Changes
- Added `DATA_PROTEIN` dataset type
- `.dat` reader supports both 320-column and 370-column (with ID) formats
- `cosine_distance()` utility in `utils.h`
- `use_cosine` flag threaded through all index structures
- IVFFlat uses spherical k-means when `use_cosine=true`

### Files Modified
- `Algorithms/AlgorithmsPart1/include/`: `parseInput.h`, `datasets.h`, `utils.h`, `lsh.h`, `hypercube.h`, `ivfflat.h`, `ivfpq.h`
- `Algorithms/AlgorithmsPart1/src/`: `parseInput.c`, `datasets.c`, `main.c`, `lsh.c`, `hypercube.c`, `ivfflat.c`, `ivfpq.c`, `runAlgorithms.c`
- `Part3/src/protein_search.py`: End-to-end Python wrapper
- `Algorithms/src/runSearchExe.py`: Fixed module imports

## Limitations
- Dimension fixed at 320 (ESM2-8M embedding size)
- Range search `-R` with cosine uses distance threshold (typical: 0.2–0.5)
- Pre-normalization optimization not yet implemented (would allow faster dot-product distance)

## References
- ESM2 protein embeddings: https://github.com/facebookresearch/esm
- Cosine similarity in vector search: cos(a,b) = (a·b) / (||a|| ||b||)
