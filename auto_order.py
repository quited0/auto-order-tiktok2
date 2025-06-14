import requests

# ==== CONFIG ====
API_KEY = "CNDM6NOEqtBJxL4vaUo7UGs8"
API_URL = "https://www.jagososmed.com/api/json.php"

SERVICE_ID = 5755
TARGET_DATA = "https://www.tiktok.com/@anishclip/video/7513911683279113490"
QUANTITY = 100

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/114.0.0.0 Safari/537.36"
}

def make_order():
    payload = {
        "api_key": API_KEY,
        "action": "order",
        "service": SERVICE_ID,
        "data": TARGET_DATA,
        "quantity": QUANTITY
    }

    try:
        response = requests.post(API_URL, data=payload, headers=HEADERS, timeout=15)
        response.raise_for_status()
        result = response.json()
        print(f"[ORDER] Response: {result}")
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] {e}")

if __name__ == "__main__":
    make_order()
