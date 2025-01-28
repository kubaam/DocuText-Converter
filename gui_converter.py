#!/usr/bin/env python3
import sys
import os
import subprocess
import importlib
import mimetypes
import tkinter as tk
from tkinter import filedialog, messagebox
import zipfile
import tempfile
import re
import textwrap

###############################################################################
# 1. Auto-install helper: tries to import a package; if not present, installs
#    it via pip, then imports again. This is "best effort" and may fail if the
#    environment does not allow pip installs.
###############################################################################

def install_and_import(package, import_name=None):
    """
    Attempt to import 'import_name' (or 'package' if import_name is None).
    If missing, install via pip, then import again.
    Returns the imported module if successful, or None if it fails.
    """
    if import_name is None:
        import_name = package

    try:
        return importlib.import_module(import_name)
    except ImportError:
        print(f"[INFO] Attempting to install '{package}' ...")
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
        except subprocess.CalledProcessError as e:
            print(f"[ERROR] Failed to install package {package}: {e}")
            return None
        # Retry import
        try:
            return importlib.import_module(import_name)
        except ImportError:
            return None

###############################################################################
# 2. Conditional imports with auto-install
###############################################################################

pdfminer = install_and_import("pdfminer.six", "pdfminer")
docx2txt = install_and_import("docx2txt")
bs4 = install_and_import("beautifulsoup4", "bs4")
lxml = install_and_import("lxml")  # for faster HTML/XML parsing
striprtf = install_and_import("striprtf")

# For .odt
odf = install_and_import("odfpy", "odf")
# .odt reading logic will rely on odfpy's low-level approach

# For images (OCR)
pytesseract = install_and_import("pytesseract")
PIL = install_and_import("Pillow", "PIL")

###############################################################################
# 3. Converter functions
###############################################################################

def convert_pdf_to_text(file_path):
    """Extract text from PDF using pdfminer.six (if available)."""
    if not pdfminer:
        return "[ERROR] pdfminer.six not installed or failed to import."
    from pdfminer.high_level import extract_text
    try:
        return extract_text(file_path)
    except Exception as e:
        return f"[ERROR] PDF text extraction failed: {e}"

def convert_docx_to_text(file_path):
    """Extract text from DOCX using docx2txt."""
    if not docx2txt:
        return "[ERROR] docx2txt is not installed or failed to import."
    try:
        return docx2txt.process(file_path)
    except Exception as e:
        return f"[ERROR] DOCX text extraction failed: {e}"

def convert_rtf_to_text(file_path):
    """Extract text from RTF using striprtf."""
    if not striprtf:
        return "[ERROR] striprtf not installed or failed to import."
    from striprtf.striprtf import rtf_to_text
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            data = f.read()
        return rtf_to_text(data)
    except Exception as e:
        return f"[ERROR] RTF text extraction failed: {e}"

def convert_html_to_text(file_path):
    """Extract text from HTML by stripping tags using BeautifulSoup."""
    if not bs4:
        return "[ERROR] beautifulsoup4 not installed or failed to import."
    from bs4 import BeautifulSoup
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            html_content = f.read()
        soup = BeautifulSoup(html_content, "lxml") if lxml else BeautifulSoup(html_content, "html.parser")
        return soup.get_text()
    except Exception as e:
        return f"[ERROR] HTML text extraction failed: {e}"

def convert_xml_to_text(file_path):
    """Extract text from XML by stripping tags using BeautifulSoup (or lxml)."""
    if not bs4:
        return "[ERROR] beautifulsoup4 not installed or failed to import."
    from bs4 import BeautifulSoup
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            xml_content = f.read()
        # Use "xml" parser or "lxml-xml" if installed
        parser = "xml"
        soup = BeautifulSoup(xml_content, parser) if lxml else BeautifulSoup(xml_content, "html.parser")
        return soup.get_text()
    except Exception as e:
        return f"[ERROR] XML text extraction failed: {e}"

def convert_odt_to_text(file_path):
    """
    Convert .odt to text using odfpy.
    We will parse the content.xml inside the ODT package.
    """
    if not odf:
        return "[ERROR] odfpy is not installed or failed to import."
    try:
        from odf.opendocument import load
        from odf.text import P

        doc = load(file_path)
        paragraphs = doc.getElementsByType(P)
        lines = []
        for p in paragraphs:
            # gather text nodes
            lines.append("".join(child.data for child in p.childNodes if child.nodeType == 3))
        return "\n".join(lines)

    except Exception as e:
        return f"[ERROR] ODT text extraction failed: {e}"

def convert_pages_to_text(file_path):
    """
    Attempt to extract text from Apple .pages file by unzipping and parsing 'index.xml' or 'QuickLook/Preview.pdf'.
    This is a best-effort approach and may not work for all .pages files.
    """
    try:
        with zipfile.ZipFile(file_path, 'r') as z:
            # Check for 'index.xml' which contains the document content
            if 'index.xml' in z.namelist():
                with z.open('index.xml') as f:
                    if not bs4:
                        return "[ERROR] beautifulsoup4 not installed or failed to import."
                    from bs4 import BeautifulSoup
                    content = f.read().decode('utf-8', errors='ignore')
                    soup = BeautifulSoup(content, "xml")
                    text = soup.get_text()
                    return text.strip()
            # Alternatively, check for 'QuickLook/Preview.pdf' and use PDF extractor
            elif 'QuickLook/Preview.pdf' in z.namelist():
                with z.open('QuickLook/Preview.pdf') as f:
                    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_pdf:
                        tmp_pdf.write(f.read())
                        tmp_pdf_path = tmp_pdf.name
                text = convert_pdf_to_text(tmp_pdf_path)
                os.remove(tmp_pdf_path)
                return text
            else:
                return "[INFO] .pages file does not contain 'index.xml' or 'QuickLook/Preview.pdf'. Cannot extract text."
    except zipfile.BadZipFile:
        return "[ERROR] Failed to open .pages file as a zip archive."
    except Exception as e:
        return f"[ERROR] .pages text extraction failed: {e}"

def convert_image_to_text(file_path):
    """Perform OCR on an image using pytesseract + Pillow."""
    if not pytesseract or not PIL:
        return "[ERROR] pytesseract or Pillow not installed. Cannot do OCR."
    try:
        from PIL import Image
        import pytesseract
        img = Image.open(file_path)
        text = pytesseract.image_to_string(img)
        return text
    except Exception as e:
        return f"[ERROR] Image OCR failed: {e}"

###############################################################################
# 4. Auto-formatting function
###############################################################################

def autoformat_text(raw_text):
    """
    Auto-format the extracted text to enhance readability.
    Steps:
    1. Normalize whitespace.
    2. Remove excessive blank lines.
    3. Wrap long lines.
    """
    if not raw_text or isinstance(raw_text, bytes):
        return raw_text

    # 1. Normalize whitespace: replace tabs with spaces, collapse multiple spaces
    text = raw_text.replace('\t', ' ')
    text = re.sub(' +', ' ', text)

    # 2. Remove excessive blank lines: keep only single blank lines
    text = re.sub(r'\n\s*\n', '\n\n', text)

    # 3. Wrap long lines to 80 characters
    wrapper = textwrap.TextWrapper(width=80, replace_whitespace=False, drop_whitespace=False)
    formatted_lines = []
    for paragraph in text.split('\n\n'):
        wrapped = wrapper.fill(paragraph.strip())
        formatted_lines.append(wrapped)
    formatted_text = '\n\n'.join(formatted_lines)

    return formatted_text

###############################################################################
# 5. Dispatcher function
###############################################################################

def convert_to_text(file_path):
    """
    Determine file type by extension or MIME type, then call the appropriate converter.
    Returns the extracted and auto-formatted text as a string.
    """
    if not os.path.isfile(file_path):
        return f"[ERROR] File not found: {file_path}"

    mime_type, _ = mimetypes.guess_type(file_path)
    ext = os.path.splitext(file_path)[1].lower()
    if mime_type is None:
        mime_type = ""

    if ext == ".pdf" or "pdf" in mime_type:
        raw_text = convert_pdf_to_text(file_path)
    elif ext == ".docx":
        raw_text = convert_docx_to_text(file_path)
    elif ext == ".doc":
        return "[ERROR] .doc (binary) format is not supported by pure Python libraries. Use external tools."
    elif ext == ".odt":
        raw_text = convert_odt_to_text(file_path)
    elif ext == ".rtf":
        raw_text = convert_rtf_to_text(file_path)
    elif ext in [".html", ".htm"] or "html" in mime_type:
        raw_text = convert_html_to_text(file_path)
    elif ext == ".xml" or "xml" in mime_type:
        raw_text = convert_xml_to_text(file_path)
    elif ext == ".pages":
        raw_text = convert_pages_to_text(file_path)
    elif ext in [".jpg", ".jpeg", ".png", ".tif", ".tiff", ".bmp", ".gif"]:
        raw_text = convert_image_to_text(file_path)
    else:
        return f"[ERROR] Unsupported or unknown file type: '{ext}' (MIME: '{mime_type}')"

    # Apply auto-formatting
    formatted_text = autoformat_text(raw_text)
    return formatted_text

###############################################################################
# 6. GUI with tkinter
###############################################################################

def select_file():
    file_path = filedialog.askopenfilename()
    if not file_path:
        return  # user canceled

    # Convert text
    text_result = convert_to_text(file_path)

    # Show the result in the text widget (clear first, then insert)
    text_box.config(state=tk.NORMAL)
    text_box.delete("1.0", tk.END)
    text_box.insert(tk.END, text_result)
    text_box.config(state=tk.DISABLED)

def save_text():
    """Save the extracted and formatted text in the text box to a .txt file."""
    # Ask user for a filename/location
    save_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if not save_path:
        return  # user canceled

    # Retrieve text from widget
    text_box.config(state=tk.NORMAL)
    text_content = text_box.get("1.0", tk.END)
    text_box.config(state=tk.DISABLED)

    try:
        with open(save_path, 'w', encoding='utf-8') as f:
            f.write(text_content.strip() + "\n")
        messagebox.showinfo("Success", f"Text saved to: {save_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save file:\n{e}")

def main():
    global text_box

    root = tk.Tk()
    root.title("Document to Text Converter")

    # Set window size
    root.geometry("800x600")

    # Frame for buttons
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    # "Select File" button
    select_button = tk.Button(button_frame, text="Select File", command=select_file, width=15)
    select_button.pack(side=tk.LEFT, padx=10)

    # "Save Text" button
    save_button = tk.Button(button_frame, text="Save Text", command=save_text, width=15)
    save_button.pack(side=tk.LEFT, padx=10)

    # Instruction Label
    instruction_label = tk.Label(root, text="Select a file to convert it to plain text. The text will be auto-formatted for readability.")
    instruction_label.pack(pady=5)

    # Scrollable text box
    text_frame = tk.Frame(root)
    text_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    text_box = tk.Text(text_frame, wrap=tk.WORD, state=tk.DISABLED)
    text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scroll = tk.Scrollbar(text_frame, command=text_box.yview)
    scroll.pack(side=tk.RIGHT, fill=tk.Y)
    text_box.config(yscrollcommand=scroll.set)

    root.mainloop()

if __name__ == "__main__":
    main()
