from __future__ import annotations
import pandas as pd

def _strip_strings(df: pd.DataFrame) -> pd.DataFrame:
    """
    Trim whitespace from all string columns.
    """
    out = df.copy()
    for col in out.select_dtypes(include=["object", "string"]).columns:
        out[col] = out[col].astype("string").str.strip()
    return out

def clean_data(df: pd.DataFrame, output_path: str = None) -> pd.DataFrame:
    """
    Clean the dataframe and optionally save to CSV if output_path is provided.
    
    Steps:
    - returns a copy (no mutation)
    - standardizes column names (lowercase, spaces -> underscores, trimmed)
    - trims whitespace in string columns
    - drops exact duplicate rows
    - drops rows that contain ANY null values
    - saves to CSV if output_path is given
    """
    out = df.copy()

    # standardize column names
    out.columns = [c.strip().lower().replace(" ", "_") for c in out.columns]

    # trim strings
    out = _strip_strings(out)

    # drop duplicates
    out = out.drop_duplicates()

    # ✅ drop rows that have ANY nulls
    out = out.dropna(how="any")

    # save to CSV if output_path is passed
    if output_path:
        out.to_csv(output_path, index=False)

    return out
