import pathlib
from typing import Iterable, List

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def plot_heatmaps_for_file(csv_path: pathlib.Path, n_values: Iterable[int]) -> List[pathlib.Path]:
    """Generate qps vs recall heatmaps for the given CSV and each requested N.

    Returns the list of generated image paths (one per N that exists in the data).
    """

    df = pd.read_csv(csv_path)
    generated: List[pathlib.Path] = []

    for n in n_values:
        subset = df[df["N"] == n]
        if subset.empty:
            continue

        plt.figure(figsize=(6, 5))
        sns.set_theme(style="whitegrid")

        sns.scatterplot(
            data=subset,
            x="qps",
            y="recall",
            color="royalblue",
            s=30,
            edgecolor="white",
        )

        plt.xlabel("Queries per second (qps)")
        plt.ylabel("Recall")
        plt.title(f"{csv_path.name} — N={n}: qps vs recall")
        plt.tight_layout()

        output_path = csv_path.with_name(f"{csv_path.stem}_N{n}_qps_recall_scatter.png")
        plt.savefig(output_path, dpi=200)
        plt.close()

        generated.append(output_path)

    return generated


def main() -> None:
    root = pathlib.Path(__file__).resolve().parents[1]
    data_dir = root / "output" / "grid_search"

    csv_files = [
        "grid_search_hypercube.csv",
        "grid_search_ivfflat.csv",
        "grid_search_ivfpq.csv",
        "grid_search_lsh.csv",
        "grid_search_nlsh.csv",
    ]

    n_values = (1, 10, 50)

    all_outputs: List[pathlib.Path] = []
    for csv_file in csv_files:
        csv_path = data_dir / csv_file
        all_outputs.extend(plot_heatmaps_for_file(csv_path, n_values))

    if all_outputs:
        print("Generated heatmaps:")
        for path in all_outputs:
            print(f"- {path.relative_to(root)}")
    else:
        print("No heatmaps generated (no matching N values in the input files).")


if __name__ == "__main__":
    main()
