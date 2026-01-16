#!/usr/bin/env python3
"""Filter BLAST outfmt 6 results by E-value and per-query top-N bit scores."""

from libraries import Dict, List, Tuple, Hit, filter_hits, write_top_hits, defaultdict, Path, csv, parse_args_blast

# -----------------------------
# Main
# -----------------------------
def main() -> None:
    # -----------------------------
    # Parse command-line arguments
    # -----------------------------
    args = parse_args_blast()
    input_path = Path(args.input)
    
    output_path = Path(args.output)
    if args.top <= 0:
        raise ValueError("--top must be a positive integer")

    # --------------------------------
    # Filter BLAST hits by E-value
    # --------------------------------
    hits_by_query = filter_hits(input_path, args.max_evalue)

    
    # -----------------------------------------------------
    # Write top N unique hits per query to output
    # -----------------------------------------------------
    write_top_hits(hits_by_query, output_path, args.top)

if __name__ == "__main__":
    main()