from concurrent.futures import ProcessPoolExecutor
import pandas as pd
from typing import Dict
from column_sum_processor import ColumnSumProcessor
from datetime import datetime



class ParallelColumnProcessor:
    def __init__(self, input_file: str, bucket_name: str, folder_name: str, 
                 minio_endpoint: str, minio_access_key: str, minio_secret_key: str, minio_region: str):
        self.input_file = input_file
        self.bucket_name = bucket_name
        self.folder_name = folder_name
        self.timestamp = datetime.now().strftime('%y%m%d-%H%M%S')

        # MinIO operations will happen outside of parallel processing
        self.column_sum_processor = ColumnSumProcessor(
            input_file=input_file,
            bucket_name=bucket_name,
            folder_name=folder_name,
            minio_endpoint=minio_endpoint,
            minio_access_key=minio_access_key,
            minio_secret_key=minio_secret_key,
            minio_region=minio_region
        )

    @staticmethod
    def process_single_column(column_name: str, column_data: pd.Series) -> Dict[str, str]:
        """Processes a single column and calculates its sum."""
        try:
            column_sum = column_data.sum()
            return {column_name: f"{int(column_sum):,}"}
        except Exception as e:
            return {column_name: f"Error: {e}"}

    def process_columns_in_parallel(self) -> Dict[str, str]:
        """Distributes the processing of columns across multiple processes."""
        # Read the input file
        df = self.column_sum_processor.read_excel_file()

        # Filter numeric columns
        numeric_df = self.column_sum_processor.filter_numeric_columns(df)

        # Pass only serialized data to the worker processes
        results = {}
        with ProcessPoolExecutor() as executor:
            futures = {
                executor.submit(self.process_single_column, column, numeric_df[column]): column
                for column in numeric_df.columns
            }
            for future in futures:
                column_name = futures[future]
                try:
                    results.update(future.result())
                except Exception as e:
                    results[column_name] = f"Error: {e}"
        return results

    def process(self) -> Dict[str, str]:
        """Orchestrates the parallel column processing and uploads results."""
        # Process columns in parallel
        column_sums = self.process_columns_in_parallel()

        # Save the results
        result_file = f"results/sum-numeric-columns-parallel-{self.timestamp}.xlsx"
        result_df = pd.DataFrame(list(column_sums.items()), columns=['Column', 'Sum'])
        self.column_sum_processor.save_to_excel(result_df, result_file)

        # Upload results file to MinIO
        self.column_sum_processor.upload_to_minio(result_file)

        return column_sums
