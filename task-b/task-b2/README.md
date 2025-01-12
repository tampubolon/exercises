# task-b2: Distributed Compute For the Win!

## Folder Structure
```bash
/app/
├── main.py                      # Entry point
├── column_sum_processor.py      # Contains the ColumnSumProcessor class
├── parallel_column_processor.py # Contains the ParallelColumnProcessor class
├── docker-compose.yml
├── Dockerfile
├── dummy-data.xlsx              # Dummy file for input
│ utils/
│   └── file_utils.py            # Utility functions
├── columns-sum/                 # Directory to store column sum result
└── results/                     # Directory to store output Excel files
```

## Installation
To run this project in your environment, run following command:
```
git clone git@github.com:tampubolon/exercises.git
cd exercise
docker-compose up --build
```

## Environment variables
create an `.env` file to store variables needed to connect to min.io server.
```
MINIO_ENDPOINT=13.228.17.32:9000
MINIO_ACCESS_KEY=minioadmin
MINIO_SECRET_KEY=minioadmin
MINIO_REGION=ap-southeast-1
```
Minio web UI is accessible from: http://13.228.17.32:9090



## `main.py`

The main entry point of the application. This script:

- Initializes the MinIO configuration and starts a resource monitoring thread.
- Loads environment variables from the `.env` file.
- Creates an instance of the `ColumnSumProcessor` class to process the Excel file.
- Displays the column sums in the console.
- Stops the monitoring thread once the processing is complete.

#### Key components:
- **Monitoring Thread**: Uses `MonitorResources` to monitor CPU and memory usage in a separate thread.
- **ColumnSumProcessor**: The main processor class that handles the Excel file, calculates column sums, and uploads the result to MinIO.

## `monitor_resources.py`

Contains the `MonitorResources` function, which monitors CPU and memory usage in real-time.

#### `MonitorResources(stop_event, bars=50)`
- **stop_event**: A threading event to stop the monitoring process.
- **bars**: Number of characters used to display the resource usage graph.

This function continuously prints the CPU and memory usage in a graphical format until the `stop_event` is set.

## `column_sum_processor.py`

Contains the `ColumnSumProcessor` class, which processes an input Excel file, calculates the sum of each numeric column, and uploads the result to a MinIO bucket.


## `parallel_column_processor.py`
The `parallel_column_processor.py` script is designed to process numeric columns in an Excel file in parallel using multiple processes. It calculates the sum of each numeric column and uploads the results to a MinIO bucket for storage.
This script is an extension of the `ColumnSumProcessor` class, leveraging parallel processing for improved performance with large datasets.<br>
Features:
- Processes numeric columns in an Excel file in parallel using `ProcessPoolExecutor`.
- Calculates the sum of each numeric column.
- Collect and aggregate results back into a final output
- Saves the results to an Excel file.
- Uploads the results to a specified MinIO bucket and folder.<br>

**`parallel_column_processor.py` Output**
- Each numeric column is processed in parallel to calculate its sum.
- Final output is the aggregate results of each columns sum, and are saved to a file named sum-numeric-columns-parallel-<timestamp>.xlsx.
- The final output file is uploaded to the specified MinIO bucket and folder.


##### Constructor:
```
ParallelColumnProcessor(input_file: str, bucket_name: str, folder_name: str, 
                        minio_endpoint: str, minio_access_key: str, minio_secret_key: str, minio_region: str)
```

