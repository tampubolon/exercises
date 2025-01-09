import pandas as pd
import subprocess
from datetime import datetime
from typing import Dict
from utils.file_utils import ensure_directory_exists

class ColumnSumProcessor:
    def __init__(self, input_file: str):
        self.input_file = input_file
        self.timestamp = datetime.now().strftime('%y%m%d-%H%M%S')
        ensure_directory_exists("results")

    def read_excel_file(self) -> pd.DataFrame:
        """Reads the Excel file into a DataFrame."""
        return pd.read_excel(self.input_file)

    def filter_numeric_columns(self, df: pd.DataFrame) -> pd.DataFrame:
        """Filters only numeric columns from the DataFrame."""
        return df.select_dtypes(include=['number'])

    def save_to_excel(self, df: pd.DataFrame, filename: str) -> None:
        """Saves a DataFrame to an Excel file and processes it with LibreOffice."""
        df.to_excel(filename, index=False)
        subprocess.run(['libreoffice', '--headless', '--convert-to', 'xlsx', filename])

    def calculate_column_sums(self, numeric_df: pd.DataFrame) -> Dict[str, str]:
        """Calculates the sum of each numeric column and formats the result."""
        column_sums = {}
        for column in numeric_df.columns:
            column_sum = numeric_df[column].sum()
            column_sums[column] = f"{int(column_sum):,}"
        return column_sums

    def process(self) -> Dict[str, str]:
        """Main processing function to compute column sums."""
        # Read the input file
        df = self.read_excel_file()

        # Filter numeric columns
        numeric_df = self.filter_numeric_columns(df)

        # Save numeric columns to a new file
        numeric_file = f"results/load-numeric-column-{self.timestamp}.xlsx"
        self.save_to_excel(numeric_df, numeric_file)

        # Calculate column sums
        column_sums = self.calculate_column_sums(numeric_df)

        # Save sums to a new file
        sum_file = f"results/sum-numeric-column-{self.timestamp}.xlsx"
        sum_df = pd.DataFrame(list(column_sums.items()), columns=['Column', 'Sum'])
        self.save_to_excel(sum_df, sum_file)

        return column_sums