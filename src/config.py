# config.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# SerpAPI Key
SERPAPI_KEY = os.getenv("SERPAPI_KEY")

# Image settings
MIN_WIDTH = 800
MIN_HEIGHT = 600
SAVE_FOLDER = "downloaded_images"
os.makedirs(SAVE_FOLDER, exist_ok=True)
