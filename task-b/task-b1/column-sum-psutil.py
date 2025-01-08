#column-sum.py with psutil feature, display_usage()

import pandas as pd
import time
import psutil
import threading

start_time = time.time()

def compute_column_sums(input_file):
    # Start measuring time

    # Read the Excel file into a DataFrame
    df = pd.read_excel(input_file)

    # Initialize a dictionary to store the sums
    column_sums = {}

    # Iterate through all columns to calculate the sum of numeric columns
    for column in df.columns:
        if pd.api.types.is_numeric_dtype(df[column]):
            column_sum = df[column].sum()
            # Convert np.int64 to plain int and format the sum with commas
            column_sums[column] = f"{int(column_sum):,}"

    return column_sums


def display_usage(stop_event, bars=20):
    print("\nMonitoring system resources. Press Ctrl+C to stop.\n")
    while not stop_event.is_set():
        cpu_usage = psutil.cpu_percent(interval=0.5)
        mem_usage = psutil.virtual_memory().percent

        cpu_percent = (cpu_usage / 100.0)
        cpu_bar = '█' * int(cpu_percent * bars) + '_' * (bars - int(cpu_percent * bars))

        mem_percent = (mem_usage / 100.0)
        mem_bar = '█' * int(mem_percent * bars) + '_' * (bars - int(mem_percent * bars))

        print(
            f"\rCPU_USAGE: |{cpu_bar}| {cpu_usage:.2f}%   MEM_USAGE: |{mem_bar}| {mem_usage:.2f}%   ",
            end="\r"
        )

# Main execution
if __name__ == "__main__":
    input_file = "dummy-data.xlsx"  #Excel Input file

    # Create a stop event for the resource monitoring thread
    stop_event = threading.Event()

    # Start resource monitoring thread
    monitor_thread = threading.Thread(target=display_usage, args=(stop_event,))
    monitor_thread.start()

    try:
        # Run compute_column_sums function
        sums = compute_column_sums(input_file)
    finally:
        # Stop resource monitoring thread
        stop_event.set()
        monitor_thread.join()

    # Print results
    print("\nColumn Sums:")
    print(sums)

    # Calculate execution time
    end_time = time.time()
    execution_time = end_time - start_time

    # Print the execution time
    print(f"\nExecution time: {execution_time:.4f} seconds")  # Print execution time to 4 decimal places    

