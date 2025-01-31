import os
import asyncio
import aiohttp
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from dotenv import load_dotenv

# Загрузка переменных окружения из файла .env
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
BASE_URL = "https://api.a1track.ru/v1"
BASE_URL2 = 'https://api.a1track.ru/v1/tokens'

# Проверка наличия токена бота
if not TELEGRAM_TOKEN:
    raise ValueError("TELEGRAM_TOKEN отсутствует в файле .env.")

# Создание объекта бота и диспетчера
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()

# Хранилище токенов пользователей
user_tokens = {}

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

# Состояния для FSM (Finite State Machine)
class AuthStates(StatesGroup):
    email = State()
    password = State()

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
    url = BASE_URL2
    payload = {"user": email, "password": password}
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=payload) as response:
            if response.status == 200:
                data = await response.json()
                return data.get("token")
            return None

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    """
    Обрабатывает команду /start и отправляет приветствие.
    """
    await message.answer("Привет! Чтобы использовать бот, выполните авторизацию с помощью команды /login.")

@dp.message(Command("login"))
async def cmd_login(message: types.Message, state: FSMContext):
    """
    Обрабатывает команду /login и запрашивает электронную почту пользователя.
    """
    await message.answer("Введите вашу электронную почту:")
    await state.set_state(AuthStates.email)

@dp.message(AuthStates.email)
async def get_email(message: types.Message, state: FSMContext):
    """
    Получает электронную почту пользователя и запрашивает пароль.
    """
    await state.update_data(email=message.text)
    await message.answer("Теперь введите ваш пароль:")
    await state.set_state(AuthStates.password)

@dp.message(AuthStates.password)
async def get_password(message: types.Message, state: FSMContext):
    """
    Получает пароль пользователя и выполняет авторизацию.
    """
    user_data = await state.get_data()
    email = user_data.get("email")
    password = message.text

    token = await authenticate_user(email, password)
    if token:
        user_tokens[message.from_user.id] = token
        await message.answer("Вы успешно авторизованы! Используйте команду /all для списка ТС.")
    else:
        await message.answer("Ошибка авторизации. Проверьте введённые данные.")

    await state.clear()

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