# scraper/image_utils.py
import os
import cv2
import requests
from PIL import Image
from io import BytesIO
from config import SAVE_FOLDER, MIN_WIDTH, MIN_HEIGHT

def download_image(url, save_path):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        image = Image.open(BytesIO(response.content)).convert("RGB")
        image.save(save_path)
        return True
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return False

def is_high_resolution(image_path, min_width=MIN_WIDTH, min_height=MIN_HEIGHT):
    try:
        image = cv2.imread(image_path)
        height, width = image.shape[:2]
        return width >= min_width and height >= min_height
    except Exception as e:
        print(f"Error reading image {image_path}: {e}")
        return False

def filter_images_from_urls(image_urls, min_width=MIN_WIDTH, min_height=MIN_HEIGHT):
    high_res_images = []
    for i, url in enumerate(image_urls):
        filename = os.path.join(SAVE_FOLDER, f"image_{i}.jpg")
        if download_image(url, filename):
            if is_high_resolution(filename, min_width, min_height):
                high_res_images.append(filename)
            else:
                os.remove(filename)
    return high_res_images
