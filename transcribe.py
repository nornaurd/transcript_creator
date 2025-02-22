import whisper

def main():
    # Завантаження моделі (можна використовувати іншу, наприклад, "small", "medium" або "large")
    model = whisper.load_model("base")
    
    # Транскрипція аудіофайлу (замість "audio_file.mp3" використовуйте ім’я вашого файлу)
    result = model.transcribe("downloaded_audio.mp3")
    
    # Отримання тексту транскрипції
    transcription_text = result["text"]
    
    # Запис результату транскрипції у текстовий файл
    with open("transcription.txt", "w", encoding="utf-8") as f:
        f.write(transcription_text)
    
    print("Транскрипцію збережено у файлі transcription.txt")

if __name__ == "__main__":
    main()
