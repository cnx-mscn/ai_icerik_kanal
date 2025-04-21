
import openai
import os
from datetime import datetime

openai.api_key = os.getenv("OPENAI_API_KEY")

def gundemlik_bilgi_uret():
    prompt = "Bugüne özel, sosyal medya için kısa, ilgi çekici ve güncel bir bilgi yaz. Maksimum 280 karakter olsun."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

if __name__ == "__main__":
    bilgi = gundemlik_bilgi_uret()
    today = datetime.now().strftime("%Y-%m-%d")
    os.makedirs(f"içerikler/{today}", exist_ok=True)
    with open(f"içerikler/{today}/metin.txt", "w", encoding="utf-8") as f:
        f.write(bilgi)
