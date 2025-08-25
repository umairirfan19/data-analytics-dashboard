"""
clean_data.py
Simple data-cleaning script for the Data Analytics Dashboard project.

Usage (from repo root):
    python scripts/clean_data.py \
        --input data/raw/sample_sales.csv \
        --output data/processed/clean_sales.csv
"""

from __future__ import annotations
import argparse
import os
from pathlib import Path

import pandas as pd


def ensure_parent_dir(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Clean a raw CSV into a tidy CSV.")
    parser.add_argument("--input", required=True, help="Path to raw CSV")
    parser.add_argument("--output", required=True, help="Path to write cleaned CSV")
    return parser.parse_args()


def clean(df: pd.DataFrame) -> pd.DataFrame:
    # 1) Standardize column names (lowercase, underscores)
    df.columns = (
        df.columns.str.strip().str.lower().str.replace(r"\s+", "_", regex=True)
    )

    # 2) Strip whitespace in string columns
    for col in df.select_dtypes(include=["object"]).columns:
        df[col] = df[col].astype(str).str.strip()

    # 3) Try converting common date columns
    for date_col in ["date", "order_date", "transaction_date"]:
        if date_col in df.columns:
            df[date_col] = pd.to_datetime(df[date_col], errors="coerce")

    # 4) Convert obvious numeric columns
    for col in df.columns:
        if any(key in col for key in ["qty", "quantity", "price", "amount", "revenue"]):
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # 5) Drop exact duplicate rows
    df = df.drop_duplicates()

    # 6) Remove rows that are completely empty
    df = df.dropna(how="all")

    # (Optional) You can choose to drop rows missing key fields
    key_cols = [c for c in ["date", "order_id", "product"] if c in df.columns]
    if key_cols:
        df = df.dropna(subset=key_cols, how="any")

    return df


def main() -> None:
    args = parse_args()
    input_path = Path(args.input)
    output_path = Path(args.output)

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    print(f"Reading: {input_path}")
    df = pd.read_csv(input_path)

    print("Cleaning data…")
    cleaned = clean(df)

    ensure_parent_dir(output_path)
    cleaned.to_csv(output_path, index=False)
    print(f"Wrote cleaned file to: {output_path}")
    print(f"Rows: {len(cleaned):,} | Columns: {len(cleaned.columns)}")


if __name__ == "__main__":
    main()
