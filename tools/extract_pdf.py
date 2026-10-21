import sys
import fitz  # pymupdf

def extract_pdf_text(pdf_path, max_chars=15000):
    doc = fitz.open(pdf_path)
    text_parts = []
    total = 0
    for i, page in enumerate(doc):
        if total >= max_chars:
            break
        page_text = page.get_text()
        text_parts.append(f"\n=== PAGE {i+1} ===\n{page_text}")
        total += len(page_text)
    doc.close()
    return "".join(text_parts)

if __name__ == "__main__":
    pdf_path = sys.argv[1]
    max_chars = int(sys.argv[2]) if len(sys.argv) > 2 else 15000
    text = extract_pdf_text(pdf_path, max_chars)
    print(text)
