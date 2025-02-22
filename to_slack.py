import requests

with open("transcription.txt", "r", encoding="utf-8") as file:
    transcription_text = file.read()

payload = {
    "username": "Lazy Assistant",  # Бот, від імені якого надсилається повідомлення
    "text": f"Транскрипція від [Валерія]:\n\n{transcription_text}"
}

webhook_url = "https://hooks.slack.com/services/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"

response = requests.post(webhook_url, json=payload)

if response.status_code == 200:
    print("Повідомлення успішно надіслано!")
else:
    print(f"Помилка при надсиланні повідомлення: {response.status_code}")
