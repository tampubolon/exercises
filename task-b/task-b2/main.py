import time
from utils.file_utils import ensure_directory_exists
from parallel_column_processor import ParallelColumnProcessor

if __name__ == "__main__":
    start_time = time.time()

    input_file = "dummy-data.xlsx"
    parallel_processor = ParallelColumnProcessor(input_file)
    column_sums = parallel_processor.process()
    
    print("") # print new line
    print("===========================================================")
    print("Column Sums:", column_sums)

    end_time = time.time()
    execution_time = end_time - start_time

    print("-----------------------------------------------------------")
    print(f"Execution time: {execution_time:.4f} seconds")
    print("===========================================================")