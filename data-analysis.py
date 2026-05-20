# data-analysis.py
"""
Enhanced data analysis script using pandas, matplotlib, and seaborn.
Features:
- Load CSV, display head and summary statistics.
- Save summary statistics to a CSV file (optional).
- Generate and save histograms for numeric columns.
- Optional seaborn style for nicer plots.
- Command‑line arguments for input file, output directory, and flags.
"""

import argparse
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def parse_args():
    parser = argparse.ArgumentParser(description="Simple data analysis utility.")
    parser.add_argument("csv_path", help="Path to the input CSV file.")
    parser.add_argument("-o", "--output", default="analysis_output", help="Directory to store generated files (plots, summary CSV).")
    parser.add_argument("-s", "--save-summary", action="store_true", help="Save summary statistics to a CSV file.")
    parser.add_argument("-p", "--save-plots", action="store_true", help="Save histogram plots as PNG files.")
    parser.add_argument("-t", "--theme", choices=["default", "darkgrid", "whitegrid", "dark", "white"], default="default", help="Seaborn theme for plots.")
    return parser.parse_args()


def main(args):
    # Ensure output directory exists
    os.makedirs(args.output, exist_ok=True)

    # Load data
    try:
        df = pd.read_csv(args.csv_path)
    except Exception as e:
        print(f"Error reading CSV: {e}")
        sys.exit(1)

    print("First 5 rows:")
    print(df.head())
    print("\nSummary statistics:")
    summary = df.describe()
    print(summary)

    # Save summary if requested
    if args.save_summary:
        summary_path = os.path.join(args.output, "summary_statistics.csv")
        summary.to_csv(summary_path)
        print(f"Summary statistics saved to {summary_path}")

    # Set seaborn theme
    if args.theme != "default":
        sns.set_theme(style=args.theme)
    else:
        sns.set()

    # Plot histograms for numeric columns
    numeric_cols = df.select_dtypes(include='number').columns
    if len(numeric_cols) == 0:
        print("No numeric columns found for histogram generation.")
        return

    for col in numeric_cols:
        plt.figure()
        sns.histplot(df[col].dropna(), kde=True, bins=30)
        plt.title(f"Histogram of {col}")
        plt.xlabel(col)
        plt.ylabel('Frequency')
        plt.tight_layout()
        if args.save_plots:
            plot_path = os.path.join(args.output, f"{col}_histogram.png")
            plt.savefig(plot_path)
            print(f"Saved plot for {col} to {plot_path}")
        else:
            plt.show()
        plt.close()

if __name__ == "__main__":
    args = parse_args()
    main(args)
