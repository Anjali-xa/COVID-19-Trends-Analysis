import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

root=Path(__file__).parent
df=pd.read_csv(root/"data"/"dataset.csv")
print("Rows:",len(df))
print("\nColumns:",list(df.columns))
print("\nMissing values:\n",df.isna().sum())
print("\nSummary:\n",df.describe(include="all").transpose())
nums=df.select_dtypes(include="number")
if not nums.empty:
    nums.hist(figsize=(12,8))
    plt.tight_layout()
    (root/"outputs").mkdir(exist_ok=True)
    plt.savefig(root/"outputs"/"numeric_distributions.png")
print("\nAnalysis complete.")
