# scraper/zip_utils.py
import os
import zipfile
from config import SAVE_FOLDER

def create_zip_of_images(image_paths, zip_name="high_res_images.zip"):
    zip_path = os.path.join(SAVE_FOLDER, zip_name)
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for file in image_paths:
            zipf.write(file, os.path.basename(file))
    return zip_path
