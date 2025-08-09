# QR Secure Scanner

**QR Secure Scanner**, QR kodları okuyup içeriğindeki URL’leri otomatik olarak [VirusTotal](https://www.virustotal.com/) üzerinden tarayan bir Python uygulamasıdır.

## Özellikler
- QR kodlardan metin veya URL okuma
- URL’leri VirusTotal API ile tarama
- Güvenli / şüpheli / zararlı URL raporu
- OpenCV QRCodeDetector kullanımı (DLL bağımlılığı yok)

## Gereksinimler
- Python 3.8+
- `opencv-python`
- `requests`

## Kurulum
```bash
pip install opencv-python requests
```

## Kullanım
```bash
python qr_reader.py
```
QR kod görselinin adını girin (ör: `qr.png`)  
Uygulama QR kodu okur, eğer URL ise VirusTotal ile tarar.

## Örnek Çıktı
```
[QR Code Content] https://www.google.com
[!] This QR contains a URL. Starting scan...
[VT] Harmless: 70, Malicious: 0, Suspicious: 0
[✓] This URL appears safe.
```

## Lisans
MIT License
