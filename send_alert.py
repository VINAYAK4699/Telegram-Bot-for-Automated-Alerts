# send_alert.py

import os
import requests
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "HTML"
    }

    try:
        response = requests.post(url, data=payload)
        if response.status_code == 200:
            print(" Message sent successfully.")
        else:
            print(f"Failed to send message: {response.text}")
    except Exception as e:
        print(f" Exception: {e}")

# Example usage
if __name__ == "__main__":
    send_telegram_message(" Hello from your Python automation script!")
