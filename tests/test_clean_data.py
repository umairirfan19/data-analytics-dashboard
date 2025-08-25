import pandas as pd
from scripts.clean_data import clean_data

def test_clean_data_removes_nulls(tmp_path):
    # Create a dummy dataset with missing values
    data = {
        "Name": ["Alice", "Bob", None],
        "Sales": [100, None, 300]
    }
    df = pd.DataFrame(data)

    # Define output path inside temporary test directory
    output_file = tmp_path / "cleaned.csv"

    # Run cleaning function
    cleaned = clean_data(df, output_file)

    # Assertions
    assert cleaned.isnull().sum().sum() == 0, "Null values should be removed"
    assert len(cleaned) < len(df), "Rows with nulls should be dropped"
    assert output_file.exists(), "Cleaned file should be saved"
