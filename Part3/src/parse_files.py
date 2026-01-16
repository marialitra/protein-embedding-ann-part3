from libraries import argparse

def parse_args_embed() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate protein embeddings using ESM2")
    parser.add_argument('-i', '--input', type=str, required=True, help='Input FASTA file')
    parser.add_argument('-o', '--output', type=str, required=True, help='Output vectors.dat file')
    parser.add_argument('-model', '--model', type=str, default='esm2_t6_8M_UR50D')
    parser.add_argument('--batch-size', type=int, default=64)
    parser.add_argument('--max-len', type=int, default=1022)

    return parser.parse_args()

def parse_args_blast() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=("Filter BLAST tabular (outfmt 6) results: keep rows with E <= max-evalue,"
            "sort per query by descending bit score, and retain top N per query."))
    parser.add_argument("-i", "--input", required=True, help="Path to BLAST outfmt 6 TSV file (no header).")
    parser.add_argument("-o", "--output", required=True, help="Path to write filtered TSV results.")
    parser.add_argument("-n", "--top", type=int, required=True, help="Keep only the top N hits per query (sorted by bit score).")
    parser.add_argument("--max-evalue", type=float, default=1e-3, help="Maximum E-value to keep (default: 1e-3).")

    return parser.parse_args()


