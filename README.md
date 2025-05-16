## 📸 High-Resolution Image Scraper

![Gradio Interface Screenshot](./docs/screenshot.png)

### 🚀 Project Overview

The **High-Resolution Image Scraper** is a Python-based tool that uses the Google Images (via [SerpAPI](https://serpapi.com/)) to fetch images based on a user-defined search query. It filters out low-resolution images and only retains those that meet a minimum resolution threshold set by the user. The project includes a **Gradio-based GUI** with dark mode and ZIP download support.

---

### 🧠 Features

* 🔍 Scrape images from **Google Images** using SerpAPI.
* 📐 Filter by **minimum resolution** (width and height).
* 🌗 **Dark Mode Toggle** UI theme.
* 🎛️ Interactive UI built with **Gradio**.
* 💾 Automatically downloads high-res images into a ZIP file.
* 🖼️ Displays images in a scrollable, responsive gallery.
* 🧑‍💻 Easy to customize and extend (add more filters, sources, etc).

---

### 📁 Project Structure

```
Image-Scraper-HighRes/
├── README.md
├── Project_Requirements_doc.md
├── team_info.md
├── src/
│   └── app.py
├── docs/
│   ├── screenshot.png
│   └── tech_stack.md
├── demo/
│   ├── demo_src/
│   └── screenshots/
```

---

### 🛠️ Tech Stack

* 🐍 Python
* 🖼️ [Gradio](https://gradio.app/)
* 🔎 [SerpAPI](https://serpapi.com/)
* 📦 OpenCV, Pillow, requests, tqdm

---

### 📥 Installation & Setup

> ✅ **Requirements:** Python 3.7+, Gradio, requests, OpenCV, PIL, tqdm, serpapi

1. **Clone the repository**

```bash
git clone https://github.com/GitHub-Aditya14Raj/Image-Scraper-HighRes.git
cd Image-Scraper-HighRes
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

> *(Manually install if `requirements.txt` is not created yet)*

```bash
pip install gradio opencv-python Pillow requests tqdm serpapi
```

3. **Set your SerpAPI Key**

Inside `src/app.py`, replace:

```python
SERPAPI_KEY = "your_actual_serpapi_key"
```

---

### 🧪 How to Run

```bash
cd src
python app.py
```

> This will open a Gradio interface in your browser.

---

### 📸 Gradio Interface (Screenshot)

![image](https://github.com/user-attachments/assets/f8b66cea-b449-4438-bc12-573c367e6d57)



### 📄 License

This project is open-source and available under the [MIT License](LICENSE).

