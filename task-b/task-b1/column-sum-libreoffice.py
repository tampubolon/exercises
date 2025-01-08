import pandas as pd
import time
import subprocess
from datetime import datetime
from typing import Dict

# Start measuring time
start_time = time.time()

def compute_column_sums(input_file: str) -> Dict[str, str]:
    # Read the Excel file into a DataFrame
    df = pd.read_excel(input_file)

    # Get current timestamp to format the file names
    timestamp = datetime.now().strftime('%y%m%d-%H%M%S')

    # Filter only numeric columns
    numeric_df = df.select_dtypes(include=['number'])

    # Save the filtered numeric columns to a new Excel file using LibreOffice Calc
    numeric_file = f"results/load-numeric-column-{timestamp}.xlsx"
    numeric_df.to_excel(numeric_file, index=False)

    # Use LibreOffice to open the new file in headless mode (to make sure it is processed properly)
    subprocess.run(['libreoffice', '--headless', '--convert-to', 'xlsx', numeric_file])

    # Initialize a dictionary to store the sums
    column_sums: Dict[str, str] = {}

    # Iterate through all numeric columns to calculate the sum
    for column in numeric_df.columns:
        column_sum = numeric_df[column].sum()
        # Convert np.int64 to plain int and format the sum with commas
        column_sums[column] = f"{int(column_sum):,}"

    # Save the dictionary of sums to another Excel file using LibreOffice Calc
    sum_file = f"results/sum-numeric-column-{timestamp}.xlsx"
    sum_df = pd.DataFrame(list(column_sums.items()), columns=['Column', 'Sum'])
    sum_df.to_excel(sum_file, index=False)

    # Use LibreOffice to open the new file in headless mode
    subprocess.run(['libreoffice', '--headless', '--convert-to', 'xlsx', sum_file])

    return column_sums

# Example usage
input_file = "dummy-data.xlsx"  # The Excel input file
sums = compute_column_sums(input_file)

print("===========================================================")
# Print the results
print("Columns Sum:")
print(sums)

# Calculate execution time
end_time = time.time()
execution_time = end_time - start_time

print("-----------------------------------------------------------")
# Print the execution time
print(f"Execution time: {execution_time:.4f} seconds")
print("===========================================================")
