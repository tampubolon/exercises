import time
from column_sum_processor import ColumnSumProcessor

if __name__ == "__main__":
    start_time = time.time()

    input_file = "dummy-data.xlsx"  # The Excel input file
    processor = ColumnSumProcessor(input_file)
    sums = processor.process()

    print("===========================================================")
    print("Columns Sum:")
    print(sums)

    end_time = time.time()
    execution_time = end_time - start_time

    print("-----------------------------------------------------------")
    print(f"Execution time: {execution_time:.4f} seconds")
    print("===========================================================")