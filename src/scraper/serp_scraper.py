# scraper/serp_scraper.py
from serpapi import GoogleSearch

def get_google_image_urls(query, num_images, api_key):
    image_urls = []
    search = GoogleSearch({
        "q": query,
        "tbm": "isch",
        "ijn": "0",
        "api_key": api_key
    })
    results = search.get_dict()

    for image_result in results.get("images_results", []):
        if "original" in image_result:
            image_urls.append(image_result["original"])
        if len(image_urls) >= num_images:
            break
    return image_urls
