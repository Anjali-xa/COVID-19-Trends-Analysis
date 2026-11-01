"""COVID-19 Trends Analysis

Reproducible starter analysis for data/dataset.csv.
Current repository data is synthetic demo data; do not interpret findings as real-world facts.
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "dataset.csv"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)


def main():
    if not DATA.exists():
        raise FileNotFoundError(f"Dataset not found: {DATA}")
    df = pd.read_csv(DATA)
    print(f"Rows: {len(df):,} | Columns: {len(df.columns)}")
    print("\nMissing values:\n", df.isna().sum())
    print(f"Duplicate rows: {df.duplicated().sum()}")
    print("\nData types:\n", df.dtypes)

    # Validate the expected starter schema before analysis.
    required = [c.strip() for c in "date, country, new_cases, new_recoveries, new_deaths".split(",")]
    missing = sorted(set(required) - set(df.columns))
    if missing:
        raise ValueError(f"Expected columns are missing: {missing}")

    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    for c in ["new_cases", "new_recoveries", "new_deaths"]:
        df[c] = pd.to_numeric(df[c], errors="coerce")
    summary = df.groupby("country")["new_cases"].sum().sort_values(ascending=False)
    trend = df.groupby(df["date"].dt.to_period("M"))["new_cases"].sum()
    ylabel = "Reported new cases"

    summary.to_csv(OUT / "segment_summary.csv", header=["value"])
    fig, ax = plt.subplots(figsize=(10, 5))
    summary.plot(kind="bar", ax=ax, title="COVID-19 Trends Analysis: segment summary")
    ax.set_ylabel(ylabel)
    ax.set_xlabel("")
    fig.tight_layout()
    fig.savefig(OUT / "segment_summary.png", dpi=160)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(10, 5))
    trend.plot(ax=ax, marker="o", title="COVID-19 Trends Analysis: trend")
    ax.set_ylabel("Reported new cases")
    ax.set_xlabel("Period / segment")
    fig.tight_layout()
    fig.savefig(OUT / "trend.png", dpi=160)
    plt.close(fig)

    print("\nSegment summary:\n", summary)
    print(f"\nOutputs saved to: {OUT}")


if __name__ == "__main__":
    main()
