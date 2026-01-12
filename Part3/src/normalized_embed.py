import libraries
from libraries import np, esm, SeqIO

# -----------------------------
# CPU optimization
# -----------------------------
libraries.os.environ['OMP_NUM_THREADS'] = '4'
libraries.os.environ['MKL_NUM_THREADS'] = '4'
libraries.torch.set_num_threads(4)

# -----------------------------
# Main
# -----------------------------
def main():
    parser = libraries.argparse.ArgumentParser(description="Generate protein embeddings using ESM2")
    parser.add_argument('-i', '--input', type=str, required=True, help='Input FASTA file')
    parser.add_argument('-o', '--output', type=str, required=True, help='Output vectors.dat file')
    parser.add_argument('-model', '--model', type=str, default='esm2_t6_8M_UR50D', help='Enter what model you want to use')
    parser.add_argument('--batch-size', type=int, default=64, help='Optionally enter the batch size')
    parser.add_argument('--max-len', type=int, default=1022, help='Optionally enter the max length')

    args = parser.parse_args()

    FASTA = args.input
    VECTORS_FILE = args.output
    VECTORS_NO_FILE = libraries.os.path.splitext(args.output)[0] +"_no_normalization.dat"
    IDS_FILE = libraries.os.path.splitext(VECTORS_FILE)[0] + "_ids.txt"
    IDS_NO_FILE = libraries.os.path.splitext(VECTORS_NO_FILE)[0] + "_ids.txt"

    BATCH_SIZE = args.batch_size
    MAX_LEN = args.max_len
    EMBED_DIM = 320
    DEVICE = libraries.torch.device("cuda" if libraries.torch.cuda.is_available() else "cpu")

    libraries.os.makedirs(libraries.os.path.dirname(VECTORS_FILE), exist_ok=True)

    # -----------------------------
    # Load model
    # -----------------------------
    model, alphabet = esm.pretrained.esm2_t6_8M_UR50D()
    model = model.to(DEVICE)
    model.eval()
    batch_converter = alphabet.get_batch_converter()

    # -----------------------------
    # Load sequences
    # -----------------------------
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

    # -----------------------------
    # Prepare outputs
    # -----------------------------
    vectors = np.memmap(
        VECTORS_FILE,
        dtype='float32',
        mode='w+',
        shape=(N, EMBED_DIM)
    )

    vectors_no = np.memmap(
        VECTORS_NO_FILE,
        dtype='float32',
        mode='w+',
        shape=(N, EMBED_DIM)
    )

    # -----------------------------
    # Inference
    # -----------------------------
    with open(IDS_FILE, 'w', encoding='ascii', errors='replace') as id_file_handle:
        with open(IDS_NO_FILE, 'w', encoding='ascii', errors='replace') as id_no_file_handle:
            with libraries.torch.no_grad():
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

                        # Now save these data before normalization to be used by the ivfpq algorithm later
                        vectors_no[idx] = emb
                        id_no_file_handle.write(batch[j][0] + '\n')

                        # Normalize the vectors in order for cosine distance metric to be correct
                        # For the rest of the algorithms!
                        norm = np.linalg.norm(emb)
                        if norm > 0:
                            emb = emb / norm

                        vectors[idx] = emb
                        id_file_handle.write(batch[j][0] + '\n')
                        idx += 1

    vectors.flush()
    vectors_no.flush()

    print(f"Saved embeddings to: {VECTORS_FILE}")
    print(f"Saved ID mapping to: {IDS_FILE}")
    print(f"Saved non-normalized embeddings to: {VECTORS_NO_FILE}")
    print(f"Saved non-normalized ID mapping to: {IDS_NO_FILE}")
    print(f"Shape: ({N}, {EMBED_DIM})")

# -----------------------------
if __name__ == "__main__":
    main()
