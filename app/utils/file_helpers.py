import os
import shutil
from fastapi import UploadFile

async def save_temp_file(upload_file: UploadFile) -> str:
    """Saves an uploaded file to a temporary path."""
    temp_path = f"temp_{upload_file.filename}"
    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)
    return temp_path

def delete_file(file_path: str):
    """Safely deletes a file if it exists."""
    if os.path.exists(file_path):
        os.remove(file_path)