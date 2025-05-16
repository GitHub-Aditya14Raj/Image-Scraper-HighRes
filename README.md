
# 🖼️ High-Resolution Google Image Scraper

A user-friendly Gradio app to scrape **high-resolution** images from Google based on a search query using **SerpAPI**. Images are filtered by resolution and available for batch download as a ZIP.

---

## 📸 Demo Screenshot

![image](https://github.com/user-attachments/assets/ed8d766f-de35-4a54-b1ea-24e85cee1166)


---

## 🚀 Features

- 🔍 Google Image scraping using SerpAPI
- 🖼️ Filter by minimum resolution (width × height)
- 💾 Download images in bulk as ZIP
- 🌙 Dark mode toggle for UI

---

## 📁 Folder Structure

```

google-image-scraper/
├── scraper/
│   ├── image\_utils.py
│   ├── serp\_scraper.py
│   ├── zip\_utils.py
│   └── **init**.py
├── app.py
├── config.py
├── .env
├── README.md
└── screenshots/ui\_screenshot.png

````

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/google-image-scraper.git
cd google-image-scraper
````

### 2. Create Virtual Environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually install:

```bash
pip install gradio google-search-results opencv-python pillow tqdm python-dotenv
```

### 4. Set up `.env` File

Create a `.env` file in the root directory and add your SerpAPI key:

```env
SERPAPI_KEY="your_api_key_here"
```

### 5. Run the App

```bash
python app.py
```

It will launch the Gradio interface in your browser.

---

## 📦 Downloaded Images

Filtered images are saved to the `downloaded_images/` folder and compressed as `high_res_images.zip` for download.

---

## 📌 Notes

* This tool uses SerpAPI which requires a valid API key.
* Make sure your free/paid SerpAPI quota is sufficient for scraping.

---

## 🧑‍💻 Author

Developed by Aditya Raj

---

## 🛡️ License

This project is licensed under the MIT License.

