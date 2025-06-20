import fitz  # PyMuPDF

class PDFTextExtractor:
    def __init__(self, pdf_path):
        self.pdf_path = pdf_path
        self.doc = fitz.open(pdf_path)

    def extract_full_text(self):
        return "\n".join(page.get_text() for page in self.doc)

    def extract_text_by_page(self):
        return [(i + 1, page.get_text()) for i, page in enumerate(self.doc)]

if __name__ == "__main__":
    extractor = PDFTextExtractor("ornek.pdf")

    print(" Tüm PDF Metni:")
    print(extractor.extract_full_text())

    print("\n Sayfa Sayfa Metin:")
    for page_num, text in extractor.extract_text_by_page():
        print(f"\n--- Sayfa {page_num} ---\n{text}")
