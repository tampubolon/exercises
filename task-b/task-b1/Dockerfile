# Use linuxserver/libreoffice as the base image
FROM linuxserver/libreoffice:latest

# Set the working directory in the container
WORKDIR /app

# Install Python, pip, and required libraries using apk
RUN apk update && \
    apk add --no-cache python3 py3-pip libpq-dev bash && \
    apk add --no-cache libreoffice && \
    python3 -m venv /venv

# Activate virtual environment and install Python dependencies
RUN . /venv/bin/activate && \
    pip install --no-cache-dir pandas openpyxl

# Copy your Python script to the container
COPY column-sum-libreoffice.py /app/column-sum-libreoffice.py

# Set the entrypoint to run your script when the container starts
ENTRYPOINT ["/venv/bin/python", "/app/column-sum-libreoffice.py"]
