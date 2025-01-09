from concurrent.futures import ProcessPoolExecutor
import pandas as pd
from typing import Dict
from column_sum_processor import ColumnSumProcessor

class ParallelColumnProcessor:
    def __init__(self, input_file: str):
        self.input_file = input_file
        self.column_sum_processor = ColumnSumProcessor(input_file)
        self.timestamp = self.column_sum_processor.timestamp

    def process_single_column(self, column_name: str, df: pd.DataFrame) -> Dict[str, str]:
        """
        Processes a single column using a new instance of ColumnSumProcessor.
        """
        temp_file = f"columns-sum/temp_{column_name}-{self.timestamp}.xlsx"
        single_column_df = df[[column_name]]
        
        # Save the single column to an Excel file
        self.column_sum_processor.save_to_excel(single_column_df, temp_file)
        
        # Read the file back and process
        numeric_df = self.column_sum_processor.filter_numeric_columns(single_column_df)
        column_sums = self.column_sum_processor.calculate_column_sums(numeric_df)
        return {column_name: column_sums[column_name]}

    def process_columns_in_parallel(self) -> Dict[str, str]:
        """
        Distributes the processing of columns across multiple processes.
        """
        # Read the full input file
        df = self.column_sum_processor.read_excel_file()
        
        # Filter numeric columns
        numeric_df = self.column_sum_processor.filter_numeric_columns(df)

        # Process each column in parallel
        results = {}
        with ProcessPoolExecutor() as executor:
            futures = {
                executor.submit(self.process_single_column, column, numeric_df): column
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
        """
        Orchestrates the parallel column processing and saves results.
        """
        # Process columns in parallel
        column_sums = self.process_columns_in_parallel()
        
        # Save the aggregated results
        result_file = f"results/sum-numeric-columns-parallel-{self.timestamp}.xlsx"
        result_df = pd.DataFrame(list(column_sums.items()), columns=['Column', 'Sum'])
        self.column_sum_processor.save_to_excel(result_df, result_file)

        return column_sums