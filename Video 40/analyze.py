import pandas as pd

df = pd.read_csv("spg.csv")

for col in df.columns:
    if pd.api.types.is_numeric_dtype(df[col]):
        print(f"--- {col} ---")
        print("Mean:", df[col].mean())
        print("Min:", df[col].min())
        print("Max:", df[col].max())
        print("Median:", df[col].median())
        print("Std:", df[col].std())
        print()
