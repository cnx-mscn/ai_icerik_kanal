
import os
import requests
from datetime import datetime

def buffer_paylas():
    today = datetime.now().strftime("%Y-%m-%d")
    with open(f"içerikler/{today}/metin.txt", "r", encoding="utf-8") as f:
        text = f.read()

    access_token = os.getenv("BUFFER_ACCESS_TOKEN")
    profile_id = os.getenv("BUFFER_PROFILE_ID")

    payload = {
        "text": text,
        "profile_ids": [profile_id],
        "scheduled_at": None,
        "now": True
    }

    headers = {
        "Authorization": f"Bearer {access_token}"
    }

    response = requests.post("https://api.bufferapp.com/1/updates/create.json", headers=headers, data=payload)
    print("Gönderim sonucu:", response.status_code, response.text)

if __name__ == "__main__":
    buffer_paylas()
