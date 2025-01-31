import os
import requests
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")
BASE_URL = "https://api.a1track.ru/v1/cars/{id}"

if not API_TOKEN:
    raise ValueError("API_TOKEN не найден в .env файле.")

# Функция для получения данных оборудования
def fetch_equipment_data(equipment_id):
    url = f"{BASE_URL}{equipment_id}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json",
    }

    try:
        response = requests.get(url, headers=headers)
        print(f"Запрос: {response.url}")
        print(f"Статус код: {response.status_code}")
        print(f"Ответ API: {response.text}")

        if response.status_code == 200:
            data = response.json()
            if not data.get("results"):
                print("Данные по указанному ID не найдены. Проверьте корректность ID оборудования.")
            else:
                print("Данные оборудования:")
                for key, value in data.items():
                    print(f"{key}: {value}")
        else:
            print(f"Ошибка: {response.status_code}. Сообщение: {response.text}")

    except Exception as e:
        print(f"Произошла ошибка при выполнении запроса: {e}")

# Основной код
equipment_id = input("Введите ID оборудования: ").strip()
fetch_equipment_data(equipment_id)
