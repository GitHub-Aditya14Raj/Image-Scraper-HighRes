# app.py
import gradio as gr
from PIL import Image
from config import SERPAPI_KEY, SAVE_FOLDER
from scraper.serp_scraper import get_google_image_urls
from scraper.image_utils import filter_images_from_urls
from scraper.zip_utils import create_zip_of_images
import os

def scrape_and_filter(query, num_images, min_width, min_height):
    # Clean the save folder
    for file in os.listdir(SAVE_FOLDER):
        os.remove(os.path.join(SAVE_FOLDER, file))

    # Scrape and filter
    urls = get_google_image_urls(query, num_images, SERPAPI_KEY)
    high_res_paths = filter_images_from_urls(urls, min_width, min_height)
    zip_path = create_zip_of_images(high_res_paths)

    return [Image.open(p) for p in high_res_paths], zip_path

dark_mode_css = """
<style>
body, .gradio-container {
    background-color: #1e1e1e !important;
    color: #ffffff !important;
}
input, textarea, select {
    background-color: #2e2e2e !important;
    color: #ffffff !important;
    border-color: #444 !important;
}
button {
    background-color: #3a3a3a !important;
    color: #ffffff !important;
    border: none !important;
}
.gr-button:hover {
    background-color: #555 !important;
}
</style>
"""

def apply_dark_mode(enabled):
    return dark_mode_css if enabled else ""

# Gradio Interface
with gr.Blocks() as demo:
    dark_mode_html = gr.HTML()

    gr.Markdown("# 🔍 High-Resolution Google Image Scraper")

    with gr.Row():
        query_input = gr.Textbox(label="Search Query", placeholder="e.g., modern house interior")
        num_slider = gr.Slider(1, 50, value=10, step=1, label="Number of Images")
        dark_mode_toggle = gr.Checkbox(label="Enable Dark Mode", value=False)

    with gr.Row():
        min_width_slider = gr.Slider(100, 2000, value=800, step=50, label="Minimum Width (px)")
        min_height_slider = gr.Slider(100, 2000, value=600, step=50, label="Minimum Height (px)")

    gallery_output = gr.Gallery(label="High-Resolution Images", columns=4)
    zip_output = gr.File(label="Download All Images as ZIP")

    run_btn = gr.Button("Run Scraper")
    run_btn.click(
        fn=scrape_and_filter,
        inputs=[query_input, num_slider, min_width_slider, min_height_slider],
        outputs=[gallery_output, zip_output]
    )

    dark_mode_toggle.change(fn=apply_dark_mode, inputs=dark_mode_toggle, outputs=dark_mode_html)

demo.launch()
