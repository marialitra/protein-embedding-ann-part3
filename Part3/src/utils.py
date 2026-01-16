from libraries import Path, Tuple, List, Dict, defaultdict, csv, esm, torch, SeqIO, Any, np

# A BLAST hit is represented as:
# (bitscore, evalue, original row fields)
Hit = Tuple[float, float, List[str]]

def filter_hits(input_path: Path, max_evalue: float) -> Dict[str, List[Hit]]:
    """
        Read a BLAST outfmt 6 file and filter hits by E-value.
        For each query sequence, all hits with an E-value less than or equal
        to `max_evalue` are collected.
    """
        
    hits_by_query: Dict[str, List[Hit]] = defaultdict(list)
    with input_path.open(newline="") as f:
        reader = csv.reader(f, delimiter="\t")

        for row in reader:
            if not row or row[0].startswith("#"):
                continue

            # BLAST outfmt 6 should have at least 12 columns
            if len(row) < 12:
                # Skip malformed rows.
                continue

            try:
                evalue = float(row[10])
                bitscore = float(row[11])
            except ValueError:
                # Skip rows with non-numeric evalue/bitscore.
                continue

            if evalue > max_evalue:
                continue

            query_id = row[0]
            hits_by_query[query_id].append((bitscore, evalue, row))

    return hits_by_query

def write_top_hits(hits_by_query: Dict[str, List[Hit]], output_path: Path, top_n: int) -> None:
    """
        Write the top N unique protein hits per query to an output file.
        Duplicate protein IDs are removed.
    """
    
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", newline="") as f:
        writer = csv.writer(f, delimiter="\t")

        for query_id, hits in hits_by_query.items():
            # Sort by descending bitscore, then ascending evalue, then subject id for determinism.
            hits.sort(key=lambda h: (-h[0], h[1], h[2][1] if len(h[2]) > 1 else ""))
            
            # Track seen proteins to avoid duplicates
            seen_proteins = set()
            unique_count = 0

            for _, _, row in hits:
                if unique_count >= top_n:
                    break
                
                # Extract protein ID from subject field (sp|ID|...)
                subject_field = row[1] if len(row) > 1 else ""
                
                if subject_field.startswith("sp|"):
                    protein_id = subject_field.split("|")[1]
                else:
                    protein_id = subject_field
                
                # Skip if we've already seen this protein
                if protein_id in seen_proteins:
                    continue
                
                seen_proteins.add(protein_id)
                writer.writerow(row)
                unique_count += 1






def load_model(DEVICE: Any) -> Tuple[torch.nn.Module, esm.data.Alphabet, callable]:
    """
        Load a pretrained ESM model and move it to the specified device.
    """
        
    model, alphabet = esm.pretrained.esm2_t6_8M_UR50D()
    model = model.to(DEVICE)
    model.eval()
    batch_converter = alphabet.get_batch_converter()

    return model, alphabet, batch_converter

def load_sequences(FASTA: str, MAX_LEN: int) -> Tuple[list, int]:
    """
        Load protein sequences from a FASTA file and truncate them to a maximum length.
        Sequences are sorted by descending length to improve batching efficiency.
    """

    data = []
    for record in SeqIO.parse(FASTA, "fasta"):
        # Extract UniProt accession from >sp|A7IC07|RBFA_XANP2
        parts = record.id.split('|')
        protein_id = parts[1] if len(parts) == 3 else record.id

        seq = str(record.seq)[:MAX_LEN]
        data.append((protein_id, seq))

    # Sort by length for efficient batching
    data.sort(key=lambda x: len(x[1]), reverse=True)
    N = len(data)

    return data, N

def save_output(VECTORS_FILE: str, N: int, EMBED_DIM: int, IDS_FILE: str, BATCH_SIZE: int, data: list,
                batch_converter: callable, DEVICE: Any, model: torch.nn.Module, alphabet: esm.data.Alphabet,
                vectors: np.memmap) -> None:
    """
        Generate embeddings for protein sequences and save them to disk.
        Embeddings are written to a memory-mapped NumPy array, and the corresponding
        protein IDs are written to a separate text file.
    """

    with open(IDS_FILE, 'w', encoding='ascii', errors='replace') as id_file_handle:
        with torch.no_grad():
            idx = 0
            for i in range(0, N, BATCH_SIZE):
                batch = data[i:i + BATCH_SIZE]

                _, _, tokens = batch_converter(batch)
                tokens = tokens.to(DEVICE)

                results = model(tokens, repr_layers=[6])
                reps = results["representations"][6]
                for j, tok in enumerate(tokens):
                    valid = (tok != alphabet.padding_idx) & \
                            (tok != alphabet.cls_idx) & \
                            (tok != alphabet.eos_idx)

                    emb = reps[j][valid].mean(dim=0).cpu().numpy()

                    vectors[idx] = emb
                    id_file_handle.write(batch[j][0] + '\n')
                    idx += 1

    vectors.flush()

    print(f"Saved embeddings to: {VECTORS_FILE}")
    print(f"Saved ID mapping to: {IDS_FILE}")
    print(f"Shape: ({N}, {EMBED_DIM})")


