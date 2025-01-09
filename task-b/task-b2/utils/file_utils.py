import os

def ensure_directory_exists(directory: str) -> None:
    """Ensures the specified directory exists."""
    os.makedirs(directory, exist_ok=True)