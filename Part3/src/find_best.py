import pandas as pd

# State the algorithm being used
algorithms = {"hypercube", "ivfflat", "ivfpq", "lsh", "nlsh"}


with open("best_parameters_results.txt", "w") as f:

    # Load your file
    for algo in algorithms:
        df = pd.read_csv(f'./output/grid_search/grid_search_{algo}.csv')

        # 1. Get the maximum value of a specific column
        max_recall = df['recall'].max()

        # 2. Get the ENTIRE ROW that contains the maximum value
        # (This helps you see which parameters led to the best result)
        best_row = df.loc[df['recall'].idxmax()]
    
        # --- Formatting for File ---
        f.write(f"Algorithm: {algo.upper()}\n")
        f.write("-"*40 + "\n")
        f.write(f"Best Recall: {max_recall:.4f}\n")

        # Convert the series to a string to write it to the file
        f.write(best_row.to_string()) 
        f.write("\n" + "="*40 + "\n\n")