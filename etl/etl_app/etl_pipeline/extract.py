import pandas as pd

def extract_csv(file_path):
    """Read data from CSV file."""
    try:
        data = pd.read_csv(file_path)
        print(f"Successfully extracted data from {file_path}")
        return data
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None
