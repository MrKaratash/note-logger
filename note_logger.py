from datetime import datetime

def not_kaydet(not_metni):
    zaman = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("notlar.txt", "a", encoding="utf-8") as dosya:
        dosya.write(f"[{zaman}] {not_metni}\n")

print("📝 Basit Not Kaydedici")
not_metni = input("Kaydedilecek notu gir: ")
not_kaydet(not_metni)
print("✅ Not başarıyla kaydedildi (notlar.txt)")
