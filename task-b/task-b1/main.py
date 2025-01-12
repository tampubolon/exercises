import time
from column_sum_processor import ColumnSumProcessor
from dotenv import load_dotenv
import os
import threading
import psutil
from typing import Callable


def MonitorResources(stop_event, bars=20):
    """Function to monitor system resources like CPU and memory usage."""
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
            end="", flush=True
        )
        time.sleep(0.5)


if __name__ == "__main__":
    # Load environment variables from .env file
    load_dotenv()

    # Set up monitoring
    stop_event = threading.Event()
    monitor_thread = threading.Thread(target=MonitorResources, args=(stop_event,))
    monitor_thread.start()  # Start monitoring in a separate thread

    try:
        # Record start time
        start_time = time.time()

        input_file = "dummy-data.xlsx"  # The Excel input file
        bucket_name = "distributed-compute"  # The MinIO bucket name
        folder_name = "task-b1"  # The folder name inside the bucket

        # Get MinIO configuration from environment variables
        minio_endpoint = os.getenv("MINIO_ENDPOINT")
        minio_access_key = os.getenv("MINIO_ACCESS_KEY")
        minio_secret_key = os.getenv("MINIO_SECRET_KEY")
        minio_region = os.getenv("MINIO_REGION")

        # Pass the MinIO configuration and other parameters to the processor
        processor = ColumnSumProcessor(
            input_file, bucket_name, folder_name, 
            minio_endpoint, minio_access_key, minio_secret_key, minio_region
        )
        sums = processor.process()

        print("\n===========================================================")
        print("Columns Sum:")
        print(sums)

        # Record end time
        end_time = time.time()
        execution_time = end_time - start_time

        print("-----------------------------------------------------------")
        print(f"Execution time: {execution_time:.4f} seconds")
        print("===========================================================")

    except KeyboardInterrupt:
        print("\n\nStopping resource monitoring due to user interruption.")
    finally:
        # Stop the monitoring thread
        stop_event.set()
        monitor_thread.join()
        print("\nResource monitoring stopped.")
