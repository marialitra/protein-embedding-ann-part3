from libraries import torch, os, np, esm, SeqIO, parse_args_embed, load_model, load_sequences, save_output

# -----------------------------
# CPU optimization
# -----------------------------
os.environ['OMP_NUM_THREADS'] = '4'
os.environ['MKL_NUM_THREADS'] = '4'
torch.set_num_threads(4)

def run_embedding_pipeline(args) -> None:
    FASTA = args.input
    VECTORS_FILE = args.output
    IDS_FILE = os.path.splitext(VECTORS_FILE)[0] + "_ids.txt"

    BATCH_SIZE = args.batch_size
    MAX_LEN = args.max_len
    EMBED_DIM = 320
    DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    os.makedirs(os.path.dirname(VECTORS_FILE), exist_ok=True)

    model, alphabet, batch_converter = load_model(DEVICE)

    data, N = load_sequences(FASTA, MAX_LEN)

    # Prepare and save the output
    vectors = np.memmap(
        VECTORS_FILE,
        dtype='float32',
        mode='w+',
        shape=(N, EMBED_DIM)
    )

    save_output(VECTORS_FILE, N, EMBED_DIM, IDS_FILE, BATCH_SIZE, data, batch_converter, DEVICE, model, alphabet, vectors)

# -----------------------------
# Main
# -----------------------------
def main() -> None:

    args = parse_args_embed()

    run_embedding_pipeline(args)

# -----------------------------
if __name__ == "__main__":
    main()