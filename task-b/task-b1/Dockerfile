# Use an official Python runtime as a base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies (pandas and openpyxl for Excel support)
RUN pip install --no-cache-dir pandas openpyxl

# Command to run the Python script
CMD ["python", "column-sum.py"]
