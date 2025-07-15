import fitz  # PyMuPDF

def extract_pdf_content(pdf_path):
    doc = fitz.open(pdf_path)
    content = []
    
    for i, page in enumerate(doc):
        blocks = page.get_text("blocks")
        for block in blocks:
            text = block[4].strip()
            if text:
                content.append({
                    "page": i + 1,
                    "text": text
                })
    return content
