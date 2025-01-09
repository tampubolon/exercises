import pandas as pd
import subprocess
import os
from datetime import datetime
from typing import Dict
from minio import Minio
from utils.file_utils import ensure_directory_exists

class ColumnSumProcessor:
    def __init__(self, input_file: str, bucket_name: str, folder_name: str, 
                 minio_endpoint: str, minio_access_key: str, minio_secret_key: str, minio_region: str):
        self.input_file = input_file
        self.timestamp = datetime.now().strftime('%y%m%d-%H%M%S')
        ensure_directory_exists("results")

        # Initialize MinIO client using environment variables
        self.minio_client = Minio(
            minio_endpoint,
            access_key=minio_access_key,
            secret_key=minio_secret_key,
            region=minio_region,
            secure=False,
        )

        self.bucket_name = bucket_name
        self.folder_name = folder_name

        # Ensure bucket exists
        if not self.minio_client.bucket_exists(self.bucket_name):
            self.minio_client.make_bucket(self.bucket_name)

    def read_excel_file(self) -> pd.DataFrame:
        """Reads the Excel file into a DataFrame."""
        return pd.read_excel(self.input_file)

    def filter_numeric_columns(self, df: pd.DataFrame) -> pd.DataFrame:
        """Filters only numeric columns from the DataFrame."""
        return df.select_dtypes(include=['number'])

    def save_to_excel(self, df: pd.DataFrame, filename: str) -> str:
        """Saves a DataFrame to an Excel file and processes it with LibreOffice."""
        df.to_excel(filename, index=False)
        subprocess.run(['libreoffice', '--headless', '--convert-to', 'xlsx', filename])
        return filename  # Return the file path to be used in upload_to_minio

    def calculate_column_sums(self, numeric_df: pd.DataFrame) -> Dict[str, str]:
        """Calculates the sum of each numeric column and formats the result."""
        column_sums = {}
        for column in numeric_df.columns:
            column_sum = numeric_df[column].sum()
            column_sums[column] = f"{int(column_sum):,}"
        return column_sums
    
    def upload_to_minio(self, file_path: str):
        """Uploads a file to the MinIO bucket and folder."""
        object_name = os.path.join(self.folder_name, os.path.basename(file_path))  # Add folder name
        self.minio_client.fput_object(self.bucket_name, object_name, file_path)
        print(f"Uploaded {file_path} to MinIO bucket {self.bucket_name} in folder {self.folder_name} as {object_name}")    

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

        # Upload numeric columns file to MinIO
        minio_file = sum_file  # Pass the correct file path
        self.upload_to_minio(minio_file)

        return column_sums