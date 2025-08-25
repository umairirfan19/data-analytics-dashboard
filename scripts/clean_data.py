# scripts/clean_data.py
import pandas as pd

def _strip_strings(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    for col in out.select_dtypes(include=["object", "string"]).columns:
        out[col] = out[col].astype("string").str.strip()
    return out

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Basic dataframe cleaning:
      - returns a copy (no mutation)
      - standardizes column names: lowercased, spaces->underscores, trimmed
      - trims whitespace in string columns
      - drops exact duplicate rows
      - drops rows that are entirely NA
    Adjust/extend as needed for your dataset.
    """
    out = df.copy()

    # standardize column names
    out.columns = [c.strip().lower().replace(" ", "_") for c in out.columns]

    # trim strings
    out = _strip_strings(out)

    # drop duplicates and all-NA rows
    out = out.drop_duplicates()
    out = out.dropna(how="all")

    return out
