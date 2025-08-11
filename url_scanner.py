import requests
import base64

API_KEY = "YOUR_API_KEY_HERE"
VT_URL = "https://www.virustotal.com/api/v3/urls"

def analyze_url(url):
    try:
        print(f"\n[+] Scanning URL with VirusTotal: {url}")

        url_id = base64.urlsafe_b64encode(url.encode()).decode().strip("=")
        headers = {
            "x-apikey": API_KEY
        }

        response = requests.get(f"{VT_URL}/{url_id}", headers=headers)
        print("[DEBUG] Raw VirusTotal response:")
        print(response.text)

        if response.status_code == 200:
            data = response.json()
            stats = data['data']['attributes']['last_analysis_stats']

            print(f"[VT] Harmless: {stats['harmless']}, Malicious: {stats['malicious']}, Suspicious: {stats['suspicious']}")

            if stats['malicious'] > 0 or stats['suspicious'] > 0:
                print("[!] This URL may be malicious!")
            else:
                print("[✓] This URL seems safe.")

        elif response.status_code == 404:
            print("[?] This URL has not been analyzed yet or is too new.")
        else:
            print(f"[X] VirusTotal API Error: {response.status_code}")

    except Exception as e:
        print(f"[X] Error during URL analysis: {e}")