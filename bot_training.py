import requests

# Функция для получения информации о транспортном средстве
def get_car_info(car_id, access_token, is_show_disabled=False):
    # URL для запроса, заменяем {id} на car_id
    url = f"https://https://api.a1track.ru/swagger/v1/swagger.json"

    # Параметры запроса
    params = {
        'IsShowDisabled': is_show_disabled
    }

    # Заголовки запроса
    headers = {
        'Authorization': f'Bearer {access_token}',  # Здесь указываем токен
    }

    try:
        # Отправляем GET-запрос к API
        response = requests.get(url, headers=headers, params=params)

        # Проверка успешности запроса
        if response.status_code == 200:
            # Возвращаем данные
            return response.json()
        else:
            # Обработка ошибки (например, если статус ответа 400 или 404)
            return f"Ошибка {response.status_code}: {response.text}"
    except Exception as e:
        return f"Произошла ошибка: {e}"

# Пример использования функции
if __name__ == "__main__":
    # Замените на ваш реальный токен доступа
    access_token = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1lIjoic2tyQHRrZ2xvbmFzcy5ydSIsInRva2VuX2lkIjoiYmM2ZDc0ZWYtNDdlNS00Nzk1LWFiOGUtZDIyZjgxMGNkYzU3IiwiY29udHJhZ2VudF9pZCI6IjMyNmEyOWFmLWFhM2QtNDBmNC05M2NhLWY5ODcxNjI0OWMzMSIsImh0dHA6Ly9zY2hlbWFzLm1pY3Jvc29mdC5jb20vd3MvMjAwOC8wNi9pZGVudGl0eS9jbGFpbXMvcm9sZSI6IkFkbWluIiwibmJmIjoxNzM3Mzc3MDYxLCJleHAiOjI1MzQwMjMwMDgwMCwiaXNzIjoicnUuYTF0cmFjay5hcGkuaXNzLmFwcC52MyIsImF1ZCI6InJ1LmExdHJhY2suYXBpLmF1ZC5hcHAifQ.bTbTSc7a4gh_0697ukTlmbink3ZkSbWtDdq5BVuXnPuMjpahVCtKuCHYloC5s8611Bdoj2NZcd9CQ7FpUZn04_HC5OBO8BD1TspRwUUCBrxjJsUzhfNbBbnZMeEqOwHm_EKAki8pTLqLCAGXrmt7yP7gfuR7nRxGnuz72eLNn7jNOoi7IQPEdpl80_ewTw8O1gr6lm7bcU9NA0exIf1gVD1T_nky7eDwxRnFVfdaWPz-sAsrlKn6rFW1om07F5aGN-HMWss-mzXRtO9N4l7ogAtbf62rrcumJlr_hz5Jt0yRg7E58FQEJC2rJ0DT8FN6Zy1H7EjDDMfnu_iaN3qFHA"

    # Введите ID транспортного средства
    car_id = input("Введите ID транспортного средства: ")

    # Получаем информацию о транспортном средстве
    car_info = get_car_info(car_id, access_token)

    # Печатаем результат
    if isinstance(car_info, dict):
        print("Информация о транспортном средстве:")
        print(car_info)
    else:
        print(car_info)
