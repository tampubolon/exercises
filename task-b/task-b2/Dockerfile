# Use linuxserver/libreoffice as the base image
FROM linuxserver/libreoffice:latest

# Set the working directory in the container
WORKDIR /app

# Install Python, pip, and required libraries using apk
RUN apk update && \
    apk add --no-cache python3 py3-pip libpq-dev bash gcc musl-dev python3-dev linux-headers && \
    apk add --no-cache libreoffice && \
    python3 -m venv /venv

# Activate virtual environment and install Python dependencies
RUN . /venv/bin/activate && \
    pip install --upgrade pip && \
    pip install --no-cache-dir pandas openpyxl minio python-dotenv psutil

# Copy the entire project into the container
COPY . /app

# Ensure the working directory is added to PYTHONPATH
ENV PYTHONPATH=/app

# Set the entrypoint to run your script when the container starts
ENTRYPOINT ["/venv/bin/python", "/app/main.py"]
