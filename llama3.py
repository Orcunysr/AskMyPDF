from openai import OpenAI
from pdf_text_extractor import PDFTextExtractor

def find_quote_page(quote: str, pages: list) -> int | None:
    """Verilen alıntıyı sayfa sayfa metinlerde arar ve hangi sayfada geçtiğini döner."""
    for page_num, text in pages:
        if quote.strip() in text:
            return page_num
    return None

class Llama3PDFQA:
    def __init__(self, pdf_path, model_name="llama3"):
        self.client = OpenAI(
            base_url='http://localhost:11434/v1',
            api_key='ollama'
        )
        self.model_name = model_name

        extractor = PDFTextExtractor(pdf_path)
        self.document_text = extractor.extract_full_text()
        self.page_texts = extractor.extract_text_by_page()

    def ask(self, question: str) -> str:
        messages = [
            {
                "role": "system",
                "content": (
                    "Aşağıdaki metne göre kullanıcıdan gelen soruyu yanıtla. "
                    "Eğer metinden alıntı yaparsan sadece o kısmı yanıtın altında 'Alıntı:' başlığıyla, "
                    'tırnak içinde ve başına 4 boşluk koyarak ayrı bir satıra yaz. '
                    "Alıntıyı doğrudan metinden birebir aktar."
                ),
            },
            {
                "role": "user",
                "content": f"Metin:\n{self.document_text[:3000]}\n\nSoru: {question}"
            }
        ]

        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=messages
        )

        raw_content = response.choices[0].message.content

        if "Alıntı:" in raw_content:
            parts = raw_content.split("Alıntı:")
            ana_cevap = parts[0].strip()
            alinti_kismi = parts[1].strip()

            satirlar = []
            for line in alinti_kismi.splitlines():
                quote = line.strip().strip('"')
                if not quote:
                    continue
                page = find_quote_page(quote, self.page_texts)
                if page:
                    satirlar.append(f'    "{quote}"\n{" " * 43}(sayfa {page})')
                else:
                    satirlar.append(f'    "{quote}"')

            alinti_formatli = "\n".join(satirlar)
            return f"{ana_cevap}\n\nAlıntı:\n{alinti_formatli}"
        else:
            return raw_content


if __name__ == "__main__":
    qa = Llama3PDFQA("ornek.pdf")
    while True:
        soru = input("\nPDF'e göre ne öğrenmek istiyorsun?\n> ")
        if soru.lower() in ["çık", "exit", "quit"]:
            break
        yanit = qa.ask(soru)
        print("\nYanıt:\n", yanit)
