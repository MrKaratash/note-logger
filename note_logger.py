from datetime import datetime
import os

def not_kaydet(not_metni):
    os.makedirs("logs", exist_ok=True)  # klasör yoksa oluştur
    zaman = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    dosya_yolu = os.path.join("logs", "notlar.txt")

    with open(dosya_yolu, "a", encoding="utf-8") as dosya:
        dosya.write(f"[{zaman}] {not_metni}\n")

print("📝 Basit Not Kaydedici")
not_metni = input("Kaydedilecek notu gir: ")
not_kaydet(not_metni)
print("✅ Not başarıyla kaydedildi (logs/notlar.txt)")
