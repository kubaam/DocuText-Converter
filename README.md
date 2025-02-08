---

# 📄 **DocuText Converter** 🖥️  

![License](https://img.shields.io/badge/license-MIT-blue.svg) ![Python](https://img.shields.io/badge/python-3.6%2B-blue.svg) ![Version](https://img.shields.io/badge/version-1.0.0-green.svg)  

## 🚀 **Table of Contents**  

- [🌟 Introduction](#-introduction)  
- [✨ Features](#-features)  
- [🔧 Installation](#-installation)  
  - [📋 Prerequisites](#-prerequisites)  
  - [📦 Clone the Repository](#-clone-the-repository)  
  - [🛠️ Install Dependencies](#️-install-dependencies)  
  - [🔍 Install Tesseract OCR](#-install-tesseract-ocr)  
- [📝 Usage Guide](#-usage-guide)  
- [📚 Supported Formats](#-supported-formats)  
- [🔗 Dependencies](#-dependencies)  
- [🤝 Contributing](#-contributing)  
- [📜 License](#-license)  
- [📞 Contact](#-contact)  
- [🖼️ Screenshots](#-screenshots)  
- [❓ Troubleshooting](#-troubleshooting)  

---

## 🌟 **Introduction**  

**DocuText Converter** is a **Python-based GUI application** designed to **extract text** from various **document formats** and **images** effortlessly. With an intuitive **Tkinter interface**, users can easily select files, preview extracted text, and save the results in a structured format.  

📄 **Convert documents & images into plain text with ease!** 📝  

---

## ✨ **Features**  

✅ **Multi-Format Support**: Converts **PDF, DOCX, RTF, HTML, XML, ODT, Apple Pages, and image files** (via OCR).  
✅ **User-Friendly GUI**: Built with **Tkinter** for a smooth experience.  
✅ **OCR Support**: Extracts text from **scanned images** and handwritten content.  
✅ **Auto-Formatting**: Removes excess spaces, normalizes whitespace, and improves readability.  
✅ **Save Functionality**: Saves extracted text to `.txt` files in just one click.  
✅ **Lightweight & Fast**: Optimized for quick execution with minimal dependencies.  

---

## 🔧 **Installation**  

### 📋 **Prerequisites**  

- **Python 3.6 or higher** – Download from [python.org](https://www.python.org/downloads/).  

### 📦 **Clone the Repository**  

```bash  
git clone https://github.com/yourusername/docutext-converter.git  
cd docutext-converter  
```  

### 🛠️ **Install Dependencies**  

```bash  
pip install -r requirements.txt  
```  

Alternatively, install packages manually:  

```bash  
pip install pdfminer.six docx2txt beautifulsoup4 lxml striprtf odfpy pytesseract Pillow  
```  

### 🔍 **Install Tesseract OCR (For Image to Text Extraction)**  

Tesseract OCR is required for processing **image files** (JPEG, PNG, TIFF, etc.).  

#### **Windows:**  
1. Download the installer from [Tesseract at UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki).  
2. Install and **add Tesseract to your system PATH**.  

#### **macOS:**  
```bash  
brew install tesseract  
```  

#### **Linux (Debian/Ubuntu):**  
```bash  
sudo apt-get update  
sudo apt-get install tesseract-ocr  
```  

---

## 📝 **Usage Guide**  

### 1️⃣ **Run the Application**  

```bash  
python3 docutext_converter.py  
```  

### 2️⃣ **Select a File**  

- Click **"Select File"** 📂  
- Choose a **document or image** to convert.  

### 3️⃣ **View Extracted Text**  

- The converted text will appear in the **GUI text box**. 👀  

### 4️⃣ **Save the Extracted Text**  

- Click **"Save Text"** 💾  
- Choose a location to save the `.txt` file.  

---

## 📚 **Supported Formats**  

### 📄 **Document Formats**  
- **PDF** (`.pdf`)  
- **Word Documents** (`.docx`)  
- **Rich Text Format** (`.rtf`)  
- **HTML & XML** (`.html`, `.htm`, `.xml`)  
- **OpenDocument Text** (`.odt`)  
- **Apple Pages** (`.pages`)  

### 🖼️ **Image Formats (OCR Enabled)**  
- **JPEG** (`.jpg`, `.jpeg`)  
- **PNG** (`.png`)  
- **TIFF** (`.tif`, `.tiff`)  
- **BMP** (`.bmp`)  
- **GIF** (`.gif`)  

---

## 🔗 **Dependencies**  

✅ **Python Libraries:**  
- `pdfminer.six` – Extract text from PDFs.  
- `docx2txt` – Extract text from DOCX files.  
- `beautifulsoup4` – Parse HTML/XML.  
- `lxml` – Faster HTML/XML parsing.  
- `striprtf` – Extract text from RTF files.  
- `odfpy` – Extract text from ODT files.  
- `pytesseract` – OCR (image-to-text conversion).  
- `Pillow` – Image processing.  
- `tkinter` – GUI framework (included with Python).  

✅ **External Dependencies:**  
- **Tesseract OCR** – Required for **image file conversion**.  

---

## 🤝 **Contributing**  

### Want to improve **DocuText Converter**? 🎉  

1. **Fork this repository**.  
2. **Create a feature branch** (`feature/new-feature`).  
3. **Commit your changes** and push to GitHub.  
4. **Submit a pull request** – We'll review and merge it!  

Contributions are **welcome & appreciated!** 🚀  

---

## 📜 **License**  

This project is licensed under the **MIT License**. See [`LICENSE`](LICENSE) for details.  

---

## 📞 **Contact & Support**  

For issues, suggestions, or support, reach out via:  

📧 **Email:** [your.email@example.com](mailto:your.email@example.com)  
🐙 **GitHub Issues:** [Report an issue](https://github.com/yourusername/docutext-converter/issues)  

---

## ❓ **Troubleshooting**  

🛑 **Common Issues & Solutions:**  

### 1️⃣ **Tesseract OCR Not Found**  
- **Issue:** `pytesseract` cannot locate Tesseract.  
- **Solution:** Ensure Tesseract is **installed & added to PATH**.  

### 2️⃣ **Missing Dependencies**  
- **Issue:** Import errors for required modules.  
- **Solution:** Run:  
  ```bash  
  pip install -r requirements.txt  
  ```  

### 3️⃣ **.doc Files Not Supported**  
- **Issue:** `.doc` (binary format) isn't working.  
- **Solution:** Convert `.doc` to `.docx` in **Microsoft Word**.  

### 4️⃣ **GUI Not Launching**  
- **Issue:** Tkinter window doesn’t open.  
- **Solution:** Ensure `tkinter` is installed.  

---

## 🔗 **Additional Resources**  

📘 **[Tesseract OCR Documentation](https://github.com/tesseract-ocr/tesseract)**  
📘 **[Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)**  
📘 **[Python Official Website](https://www.python.org/)**  

---

🔥 **Happy Document Converting!** 🎉  

---

<!--
- DocuText Converter
- Best DocuText Converter Tool
- DocuText File Converter 2024
- Automated DocuText Conversion Software
- Free DocuText Converter Download
- DocuText to PDF Converter
- DocuText to Word Converter Tool
- DocuText File Conversion for Windows
- DocuText File Converter for MacOS
- Convert DocuText to Rich Text Format
- DocuText to Text Converter
- DocuText to HTML Converter
- DocuText to CSV Converter
- DocuText to PowerPoint Converter
- DocuText to Excel Converter Tool
- Convert DocuText to Image Files
- Batch DocuText File Converter
- DocuText Document Converter Software
- Free Online DocuText Converter
- DocuText File Conversion Service
- Convert DocuText to Multiple Formats
- Best DocuText Conversion Solution
- DocuText Conversion for Large Files
- DocuText File Converter for Business
- DocuText to PDF Converter Free Download
- DocuText File Format Converter Tool
- Fast DocuText Conversion Software
- DocuText to Word Converter Free
- DocuText to Text File Conversion
- DocuText Conversion Software for Mac
- How to Convert DocuText Files
- DocuText to DOCX Conversion Tool
- Easy DocuText File Converter
- Reliable DocuText to PDF Converter
- Convert DocuText to RTF Format
- DocuText File Converter Online Tool
- DocuText to EPUB Converter
- DocuText File to Image Conversion Tool
- Convert DocuText to LaTeX Format
- DocuText Conversion for Professionals
- High-Quality DocuText Converter Software
- DocuText File Converter with Batch Support
- Convert DocuText Files to Rich Text Format
- DocuText to XML File Converter
- DocuText File Conversion Made Easy
- DocuText File Converter for Developers
- DocuText File Converter with Cloud Integration
- Advanced DocuText Conversion Tool
- DocuText to CSV File Conversion
- DocuText to Excel File Converter 2024
- DocuText Conversion for Legal Documents
- DocuText File Converter with Encryption Support
- Free DocuText to PDF Conversion Tool
- DocuText to Plain Text Conversion
- DocuText File Converter for Data Processing
- DocuText to JSON Conversion Tool
- DocuText to Markdown Converter
- Convert DocuText to Audio Files
- DocuText to TXT File Converter
- Best Online DocuText Converter
- DocuText File Converter for Academic Use
- Convert DocuText Files for Printing
- Secure DocuText Conversion for Confidential Files
- DocuText to PDF with Formatting Retention
- Convert DocuText Files for Mobile Devices
- DocuText File Conversion Tool for Teams
- DocuText to Word with Style Retention
- Automated DocuText to PDF Conversion
- DocuText to Presentation File Converter
- DocuText File Conversion for Archive
- DocuText File Converter for Cloud Storage
- Multi-Format DocuText Converter Tool
- Quick DocuText File Converter for Work
- Convert DocuText Files in Bulk
- DocuText to PDF Conversion Made Simple
- DocuText File Conversion for Reports
- DocuText File Converter with Batch Mode
- Convert DocuText to HTML for Websites
- DocuText File Converter for Educational Use
- Convert DocuText to SVG Format
- DocuText Converter with OCR Support
-->
