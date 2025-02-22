import requests

AIRTABLE_API_KEY = "patXlNVF2wrDPaW0G.97fe66f8329320d5fc6f2f1a426f96d47565c0dfb23d363917d6958d45ad9524"
BASE_ID = "app5BVW2KouwFaEYx"
TABLE_NAME = "AudioList"  # Назва таблиці в Airtable
FIELD_NAME = "Media"      # Назва поля з прикріпленим файлом

def download_mp3_from_airtable():
    # Формуємо URL для запиту до таблиці
    url = f"https://api.airtable.com/v0/{BASE_ID}/{TABLE_NAME}"

    # Заголовки для авторизації через офіційний API
    headers = {
        "Authorization": f"Bearer {AIRTABLE_API_KEY}"
    }

    # Виконуємо GET-запит, щоб отримати записи
    response = requests.get(url, headers=headers)

    # Перевіряємо, чи успішний запит
    if response.status_code == 200:
        data = response.json()

        # Перебираємо записи
        for record in data.get("records", []):
            fields = record.get("fields", {})
            # Перевіряємо, чи є у записі поле з назвою FIELD_NAME
            if FIELD_NAME in fields:
                attachments = fields[FIELD_NAME]
                # Для прикладу візьмемо перший файл
                if attachments and isinstance(attachments, list):
                    attachment_url = attachments[0].get("url")
                    if attachment_url:
                        # Завантажуємо файл
                        file_response = requests.get(attachment_url)
                        if file_response.status_code == 200:
                            # Зберігаємо файл
                            with open("downloaded_audio.mp3", "wb") as f:
                                f.write(file_response.content)
                            print("Файл успішно завантажено!")
                            return
                        else:
                            print(f"Помилка при завантаженні файлу: {file_response.status_code}")
                            return
        print("Не знайдено записів з файлом у полі Media.")
    else:
        print(f"Помилка при отриманні записів: {response.status_code}")

if __name__ == "__main__":
    download_mp3_from_airtable()
