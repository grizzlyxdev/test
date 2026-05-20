# data-analysis.py
"""
Simple data analysis script using pandas.
It reads a CSV file, shows basic statistics, and plots a histogram.
"""

import pandas as pd
import matplotlib.pyplot as plt
import sys

def main(csv_path: str):
    # Load data
    df = pd.read_csv(csv_path)
    print("First 5 rows:")
    print(df.head())
    print("\nSummary statistics:")
    print(df.describe())
    # Plot histogram for each numeric column
    numeric_cols = df.select_dtypes(include='number').columns
    for col in numeric_cols:
        plt.figure()
        df[col].hist(bins=30)
        plt.title(f"Histogram of {col}")
        plt.xlabel(col)
        plt.ylabel('Frequency')
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python data-analysis.py <path_to_csv>")
        sys.exit(1)
    main(sys.argv[1])
