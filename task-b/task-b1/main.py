import time
from column_sum_processor import ColumnSumProcessor
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

if __name__ == "__main__":
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
    processor = ColumnSumProcessor(input_file, bucket_name, folder_name, minio_endpoint, minio_access_key, minio_secret_key, minio_region)
    sums = processor.process()

    print("===========================================================")
    print("Columns Sum:")
    print(sums)

    end_time = time.time()
    execution_time = end_time - start_time

    print("-----------------------------------------------------------")
    print(f"Execution time: {execution_time:.4f} seconds")
    print("===========================================================")