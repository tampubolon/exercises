# task-b1: Implement the Core IP

```bash
## Folder Structure
/app/
├── main.py                 # Entry point
├── column_sum_processor.py # Contains the ColumnSumProcessor class
├── docker-compose.yml
├── Dockerfile
├── dummy-data.xlsx         # Dummy file for input
│ utils/
│   └── file_utils.py       # Utility functions
└── results/                # Directory to store output Excel files
```

## Installation
To run this project in your environment, run following command:
```
git clone git@github.com:tampubolon/exercises.git
cd exercise/task-b/task-b1
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
![image](https://github.com/user-attachments/assets/3c7d9a15-435c-43be-a2c4-18b269a3bbe9)



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

This function continuously prints the CPU and memory usage in a graphical format until the `stop_event` is set.<br>
**Monitoring CPU and Memory usage with MonitorResources() class:**
![image](https://github.com/user-attachments/assets/b587da07-6cbd-4873-8df9-aa7d6b5cd849)<br>



## `column_sum_processor.py`

Contains the `ColumnSumProcessor` class, which processes an input Excel file, calculates the sum of each numeric column, and uploads the result to a MinIO bucket.

##### Constructor:
```
python
__init__(self, input_file: str, bucket_name: str, folder_name: str, 
         minio_endpoint: str, minio_access_key: str, minio_secret_key: str, minio_region: str)
```


