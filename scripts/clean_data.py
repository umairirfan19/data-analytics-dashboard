from __future__ import annotations
def clean_data(df: pd.DataFrame, output_path: str = None) -> pd.DataFrame:
    """
    Clean the dataframe and optionally save to CSV if output_path is provided.
    """
    out = df.copy()

    # standardize column names
    out.columns = [c.strip().lower().replace(" ", "_") for c in out.columns]

    # trim strings
    out = _strip_strings(out)

    # drop duplicates and all-NA rows
    out = out.drop_duplicates()
    out = out.dropna(how="all")

    # ✅ new: save to CSV if output_path is passed
    if output_path:
        out.to_csv(output_path, index=False)

    return out
