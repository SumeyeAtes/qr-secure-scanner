import os
import ctypes

# Load DLL from current directory
dll_path = os.path.join(os.path.dirname(__file__), "libzbar-64.dll")
ctypes.cdll.LoadLibrary(dll_path)

import cv2
from pyzbar.pyzbar import decode
from url_scanner import analyze_url

def read_qr(file_path):
    try:
        img = cv2.imread(file_path)
        if img is None:
            print(f"[X] File not found or could not be opened: {file_path}")
            return

        result = decode(img)

        if not result:
            print("[!] No QR code found.")
            return

        for obj in result:
            data = obj.data.decode("utf-8")
            print(f"[QR Code Content] {data}")

            if data.startswith("http"):
                print("[!] This QR contains a URL. Starting scan...")
                analyze_url(data)
    except Exception as e:
        print(f"[Error] An unexpected error occurred: {e}")

if __name__ == "__main__":
    print("Enter the QR image file name (example: qr.png): ")
    path = input()
    read_qr(path)