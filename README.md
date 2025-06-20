# AskMyPDF
# PDF Soru-Cevap Asistanı (LLaMA3 ile)

Bu proje, PDF belgeleri üzerinden anlamlı sorular sormanıza olanak tanıyan bir yerel LLM (LLaMA3) tabanlı asistandır. Kullanıcı tarafından sorulan sorulara, PDF içeriğine dayanarak yanıt verir ve doğrudan metinden alıntı yapar.

## ✨ Özellikler

- PDF içeriğini metne dönüştürür (sayfa sayfa).
- Kullanıcının sorusunu LLaMA3 modeline gönderir.
- Cevap içindeki alıntıları 4 boşluk girintili, `"` içinde gösterir.
- Alıntının geçtiği **PDF sayfa numarasını** sağ alt köşede belirtir.
- Tamamen **offline** çalışır (`Ollama` + `localhost`).

## 🛠 Gereksinimler

```bash
pip install -r requirements.txt
