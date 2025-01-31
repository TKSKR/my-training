import os
import asyncio
import aiohttp
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
BASE_URL = "https://api.a1track.ru/v1"

# Проверка наличия токена бота
if not TELEGRAM_TOKEN:
    raise ValueError("TELEGRAM_TOKEN отсутствует в файле .env.")

# Создание объекта бота и диспетчера
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

# Хранилище токенов пользователей
user_tokens = {}
# Хранилище для временного сохранения email пользователя
user_emails = {}

# Словарь перевода ключей данных
TRANSLATION = {
    "id": "Идентификатор",
    "deviceId": "ID устройства",
    "deviceNumber": "Номер устройства",
    "contragentId": "ID контрагента",
    "model": "Модель",
    "carNumber": "Госномер",
    "vinNumber": "VIN номер",
    "carType": "Тип ТС",
    "carEnabledState": "Состояние ТС",
    "isEnabled": "Активировано",
    "comment": "Комментарий",
    "carGroupIds": "Группы ТС",
}

def translate_data(data):
    """
    Переводит ключи данных на русский язык.
    :param data: Словарь данных
    :return: Переведённый словарь
    """
    return {TRANSLATION.get(k, k): v for k, v in data.items()}

async def fetch_vehicles(token):
    """
    Запрашивает список транспортных средств из API.
    :param token: Токен авторизации пользователя
    :return: Список транспортных средств
    """
    headers = {"Authorization": f"Bearer {token}"}
    url = f"{BASE_URL}/cars/my"
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                data = await response.json()
                return data.get("results", [])
            return []

async def authenticate_user(email, password):
    """
    Выполняет авторизацию пользователя и получает токен.
    :param email: Электронная почта пользователя
    :param password: Пароль пользователя
    :return: Токен авторизации или None
    """
    url = f"{BASE_URL}/tokens"
    payload = {"user": email, "password": password}
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload) as response:
            if response.status == 200:
                data = await response.json()
                return data.get("bearerToken")
            return None

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    """
    Обрабатывает команду /start и отправляет приветствие.
    """
    await message.answer("Привет! Чтобы использовать бот, выполните авторизацию с помощью команды /login.")

@dp.message(Command("login"))
async def cmd_login(message: types.Message):
    """
    Обрабатывает команду /login и запрашивает электронную почту пользователя.
    """
    await message.answer("Введите вашу электронную почту:")

@dp.message(lambda message: message.from_user.id not in user_emails)
async def get_email(message: types.Message):
    """
    Получает электронную почту пользователя.
    """
    user_emails[message.from_user.id] = message.text
    await message.answer("Теперь введите ваш пароль:")

@dp.message(lambda message: message.from_user.id in user_emails)
async def get_password(message: types.Message):
    """
    Получает пароль пользователя и выполняет авторизацию.
    """
    email = user_emails.get(message.from_user.id)
    password = message.text
    token = await authenticate_user(email, password)

    if token:
        user_tokens[message.from_user.id] = token
        await message.answer("Вы успешно авторизованы! Используйте команду /all для списка ТС.")
    else:
        await message.answer("Ошибка авторизации. Проверьте введённые данные.")

@dp.message(Command("all"))
async def list_all_vehicles(message: types.Message):
    """
    Обрабатывает команду /all и отправляет список транспортных средств.
    """
    user_id = message.from_user.id
    token = user_tokens.get(user_id)

    if not token:
        await message.answer("Вы не авторизованы. Используйте команду /login для авторизации.")
        return

    vehicles = await fetch_vehicles(token)
    if not vehicles:
        await message.answer("Список транспортных средств пуст или не удалось получить данные.")
        return

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text=vehicle["carNumber"], callback_data=f"vehicle_{vehicle['id']}")]
        for vehicle in vehicles
    ])
    await message.answer("Выберите транспортное средство:", reply_markup=keyboard)

@dp.callback_query(lambda c: c.data and c.data.startswith("vehicle_"))
async def vehicle_details(callback: types.CallbackQuery):
    """
    Обрабатывает выбор транспортного средства и отправляет информацию.
    """
    user_id = callback.from_user.id
    token = user_tokens.get(user_id)

    if not token:
        await callback.message.answer("Вы не авторизованы. Используйте команду /login для авторизации.")
        await callback.answer()
        return

    vehicle_id = callback.data.split("_")[1]
    headers = {"Authorization": f"Bearer {token}"}
    url = f"{BASE_URL}/cars/{vehicle_id}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            if response.status == 200:
                vehicle = await response.json()
                translated_vehicle = translate_data(vehicle)  # Переводим данные на русский язык
                formatted_info = "\n".join(f"{k}: {v}" for k, v in translated_vehicle.items())
                await callback.message.answer(f"Информация о транспортном средстве:\n{formatted_info}")
            else:
                await callback.message.answer("Не удалось получить информацию о транспортном средстве.")

    await callback.answer()

async def main():
    """
    Основная функция запуска бота.
    """
    print("Бот запущен. Нажмите Ctrl+C для остановки.")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())