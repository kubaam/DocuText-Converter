# 📄 DocuText Converter 🖥️

![License](https://img.shields.io/badge/license-MIT-blue.svg) ![Python](https://img.shields.io/badge/python-3.6%2B-blue.svg) ![Version](https://img.shields.io/badge/version-1.0.0-green.svg)

## 🚀 Table of Contents

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

## 🌟 Introduction

**DocuText Converter** is a powerful and user-friendly **Python GUI application** designed to seamlessly convert various **document formats** into plain text. Whether you're working with PDFs, DOCX files, RTFs, HTMLs, XMLs, ODTs, Apple Pages, or images, **DocuText Converter** simplifies the process of extracting and formatting text. With its intuitive **Tkinter interface**, you can effortlessly select files, view extracted text, and save it in a clean, readable format. 📄➡️📝

## ✨ Features

- **🔄 Automatic Dependency Installation:** Automatically installs required packages if they're missing.
- **📂 Wide Format Support:** Converts PDFs, DOCX, RTF, HTML, XML, ODT, Apple Pages, and image files (OCR).
- **🖥️ User-Friendly GUI:** Built with Tkinter for easy file selection and text viewing.
- **🛠️ Auto-Formatting:** Enhances readability by normalizing whitespace, removing excessive blank lines, and wrapping long lines.
- **💾 Save Functionality:** Allows saving the extracted text to a `.txt` file with ease.
- **🧩 Modular Design:** Easy to extend and customize for additional functionalities.

## 🔧 Installation

### 📋 Prerequisites

- **Python 3.6 or Higher:** Ensure you have Python installed. Download it from [python.org](https://www.python.org/downloads/).

### 📦 Clone the Repository

```bash
git clone https://github.com/yourusername/docutext-converter.git
cd docutext-converter
```

### 🛠️ Install Dependencies

The script includes an **auto-install** feature for dependencies. However, to manually install them, use the provided `requirements.txt`:

```bash
pip install -r requirements.txt
```

*Alternatively, install them individually:*

```bash
pip install pdfminer.six docx2txt beautifulsoup4 lxml striprtf odfpy pytesseract Pillow
```

### 🔍 Install Tesseract OCR

**Pytesseract** requires **Tesseract OCR** to be installed on your system.

- **Windows:**
  - Download the installer from [Tesseract at UB Mannheim](https://github.com/UB-Mannheim/tesseract/wiki).
  - Run the installer and follow the setup instructions.
  - Add Tesseract to your system PATH or specify the Tesseract executable path in your script.

- **macOS:**
  ```bash
  brew install tesseract
  ```

- **Linux (Debian/Ubuntu):**
  ```bash
  sudo apt-get update
  sudo apt-get install tesseract-ocr
  ```

## 📝 Usage Guide

1. **Run the Application:**

   Navigate to the project directory and execute the script:

   ```bash
   python3 docutext_converter.py
   ```

2. **Select a File:**

   - Click the **"Select File"** button. 📂
   - Choose the document or image you wish to convert to text.

3. **View Extracted Text:**

   - The extracted and auto-formatted text will appear in the text box within the GUI. 👀

4. **Save the Text:**

   - Click the **"Save Text"** button. 💾
   - Choose the destination and filename to save the extracted text as a `.txt` file.

## 📚 Supported Formats

- **📄 Documents:**
  - PDF (`.pdf`)
  - Word Document (`.docx`)
  - Rich Text Format (`.rtf`)
  - HTML (`.html`, `.htm`)
  - XML (`.xml`)
  - OpenDocument Text (`.odt`)
  - Apple Pages (`.pages`)

- **🖼️ Images:**
  - JPEG (`.jpg`, `.jpeg`)
  - PNG (`.png`)
  - TIFF (`.tif`, `.tiff`)
  - BMP (`.bmp`)
  - GIF (`.gif`)

## 🔗 Dependencies

- **Python Libraries:**
  - `pdfminer.six`: Extract text from PDF files.
  - `docx2txt`: Extract text from DOCX files.
  - `beautifulsoup4`: Parse HTML and XML files.
  - `lxml`: Faster HTML/XML parsing (optional but recommended).
  - `striprtf`: Extract text from RTF files.
  - `odfpy`: Parse ODT files.
  - `pytesseract`: Perform OCR on image files.
  - `Pillow`: Image processing required by `pytesseract`.
  - `tkinter`: Graphical User Interface (usually included with Python).

- **External Dependencies:**
  - **Tesseract OCR:** Required for converting images to text. [Installation Instructions](#-install-tesseract-ocr)

## 🤝 Contributing

Contributions are **welcome**! If you'd like to enhance **DocuText Converter**, please follow these steps:

1. **Fork the Repository:**

   Click the **"Fork"** button at the top right of this page.

2. **Create a New Branch:**

   ```bash
   git checkout -b feature/YourFeatureName
   ```

3. **Commit Your Changes:**

   ```bash
   git commit -m "Add some feature"
   ```

4. **Push to the Branch:**

   ```bash
   git push origin feature/YourFeatureName
   ```

5. **Open a Pull Request:**

   Navigate to your forked repository and click **"New Pull Request."**

Please ensure your code follows the project's coding standards and includes relevant tests. 🧪

## 📜 License

This project is licensed under the [MIT License](LICENSE). You are free to use, modify, and distribute this software as per the license terms. 📝

## 📞 Contact

For any questions, suggestions, or support, please reach out to [your.email@example.com](mailto:your.email@example.com). I'm here to help! 🤗

---

## 🖼️ Screenshots

### 🖥️ Application Interface

![GUI Screenshot](screenshots/gui.png)

*User-friendly interface for converting documents to text.*

### 📂 Selecting a File

![Select File](screenshots/select_file.png)

*Choose your document or image file to convert.*

### 💾 Saving Extracted Text

![Save Text](screenshots/save_text.png)

*Easily save your extracted text to a `.txt` file.*

---

## ❓ Troubleshooting

**🛑 Common Issues & Solutions:**

1. **Tesseract OCR Not Found:**
   - **Issue:** `pytesseract` cannot locate Tesseract OCR.
   - **Solution:** Ensure Tesseract is installed and added to your system PATH. Refer to the [Installation Instructions](#-install-tesseract-ocr).

2. **Missing Dependencies:**
   - **Issue:** Certain Python packages are not installed.
   - **Solution:** Run `pip install -r requirements.txt` to install all necessary dependencies.

3. **Unsupported .doc Files:**
   - **Issue:** `.doc` (binary) format is not supported.
   - **Solution:** Use `.docx` format or convert `.doc` files to `.docx` using Microsoft Word or other tools.

4. **Extraction Errors:**
   - **Issue:** Errors during text extraction from specific file types.
   - **Solution:** Ensure the file is not corrupted and is supported. Check for relevant package installations.

5. **GUI Not Launching:**
   - **Issue:** Tkinter window fails to open.
   - **Solution:** Verify that Tkinter is installed and properly configured with your Python installation.

*If you encounter any other issues, feel free to [open an issue](https://github.com/yourusername/docutext-converter/issues) on GitHub.*

---

🔗 **Stay Connected:**

- **GitHub:** [yourusername/docutext-converter](https://github.com/yourusername/docutext-converter)
- **Email:** [your.email@example.com](mailto:your.email@example.com)

Thank you for using **DocuText Converter**! 🙏 Your support helps improve the project. Happy converting! 🎉

---

## 📄 Additional Resources

- **[Tesseract OCR Documentation](https://github.com/tesseract-ocr/tesseract)**
- **[Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)**
- **[Python Official Website](https://www.python.org/)**
- **[Beautiful Soup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)**
- **[pdfminer.six Documentation](https://pdfminersix.readthedocs.io/en/latest/)**

---
