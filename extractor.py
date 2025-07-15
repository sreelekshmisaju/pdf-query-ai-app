import fitz  # PyMuPDF

def extract_pdf_content(pdf_path):
    doc = fitz.open(pdf_path)
    content = []

    for page_num, page in enumerate(doc, start=1):
        text = page.get_text("text")
        if text.strip():
            content.append({
                "page": page_num,
                "text": text.strip()
            })

    return content
