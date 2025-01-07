import pandas as pd
import time

def compute_column_sums(input_file):
    # Start measuring time
    start_time = time.time()

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

    # Calculate execution time
    end_time = time.time()
    execution_time = end_time - start_time

    # Explicitly print the execution time
    print(f"Execution time: {execution_time:.4f} seconds")  # Print execution time to 4 decimal places

    return column_sums

# Example usage
input_file = "dummy-data.xlsx"  # The Excel file from the previous script
sums = compute_column_sums(input_file)

# Print the results
print(sums)
