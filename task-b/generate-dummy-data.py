import random
import string
from openpyxl import Workbook

# Function to generate a random string of a specified length
def random_string(length=5):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def create_excel_with_openpyxl(output_file, rows=500000):
    # Create a new workbook and activate the default sheet
    wb = Workbook()
    ws = wb.active

    # Add column headers
    columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    for col in columns:
        ws[f'{col}1'] = col

    # Generate random data for each column and each row
    for row in range(2, rows + 2):  # Start from row 2 to row 10001
        for col_index in range(10):  # There are 10 columns (A to J)
            col = columns[col_index]

            # Add random integers or strings based on the column
            if col_index % 2 == 0:  # Even index columns (A, C, E, G, I) will have integers
                ws[f'{col}{row}'] = random.randint(100, 999)  # 3-digit integers
            else:  # Odd index columns (B, D, F, H, J) will have random strings
                ws[f'{col}{row}'] = random_string(5)  # Random 5-character string

    # Save the Excel file
    wb.save(output_file)
    print(f"Excel file created: {output_file}")
    

# Example usage
create_excel_with_openpyxl("task-b1/dummy-data.xlsx")
create_excel_with_openpyxl("task-b2/dummy-data.xlsx")
