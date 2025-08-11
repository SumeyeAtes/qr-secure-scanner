📌 QR Secure Scanner
QR Secure Scanner is a Python application that scans QR codes and automatically checks any embedded URLs against VirusTotal.

✨ Features
📷 Read text or URLs from QR codes

🌐 Scan URLs via VirusTotal API

🛡 Report Safe / Suspicious / Malicious URLs

⚡ Uses OpenCV QRCodeDetector (No DLL dependency)

💻 Simple command-line interface

📦 Requirements
Python 3.8+

Dependencies:

opencv-python

requests

python-dotenv (optional – for reading API key from .env)

🚀 Installation

1️⃣ Install required libraries:

pip install opencv-python requests python-dotenv


2️⃣ Get your VirusTotal API key:
📄 VirusTotal API Key Guide

3️⃣ Create a .env file:
VT_API_KEY=your-api-key-here

▶️ Usage
python qr_reader.py

When prompted, enter the QR code image filename:
qr.png

📌 Example Output
[QR Code Content] https://www.google.com
[!] This QR contains a URL. Starting scan...
[VT] Harmless: 70, Malicious: 0, Suspicious: 0
[✓] This URL appears safe.

📂 Project Structure
qr_reader.py       → Reads QR codes and starts scanning
url_scanner.py     → VirusTotal API client
requirements.txt   → Dependency list
.env.example       → Example API key file
.gitignore         → Excludes unnecessary files

📝 License
This project is licensed under the MIT License.
© 2025 Sumeye Ates
