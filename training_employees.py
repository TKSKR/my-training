# База данных сотрудников
employees = {
    "Иван": {
        "Иванов": {
            "password": "password123",
            "position": "Менеджер"
        }
    },
    "Анна": {
        "Петрова": {
            "password": "qwerty456",
            "position": "Аналитик"
        }
    },
    "Алексей": {
        "Сидоров": {
            "password": "123456",
            "position": "Разработчик"
        }
    }
}

# Функция для ввода имени
def get_valid_name(prompt):
    while True:
        name = input(prompt).strip().capitalize()
        if name.isalpha():
            return name
        print("Имя должно содержать только буквы. Попробуйте снова.")

# Функция для проверки имени
def check_name_in_database():
    while True:
        name = get_valid_name("Введите имя сотрудника: ")
        if name in employees:
            print("Имя найдено в базе.")
            return name
        print("Такого имени нет в базе. Попробуйте снова.")

# Функция для проверки фамилии
def check_surname_in_database(name):
    while True:
        surname = get_valid_name("Введите фамилию сотрудника: ")
        if surname in employees[name]:
            print("Фамилия найдена в базе.")
            return surname
        print("Такого сотрудника не существует. Попробуйте снова.")

# Функция для проверки пароля
def check_password(name, surname):
    while True:
        password = input("Введите пароль: ").strip()
        if password.lower() == employees[name][surname]["password"].lower():
            print("Пароль верный.")
            return
        print("Пароль введен неверно. Попробуйте снова.")

# Основной код
def main():
    name = check_name_in_database()
    surname = check_surname_in_database(name)
    check_password(name, surname)
    position = employees[name][surname]["position"]
    print(f"Привет, {position} {name} {surname}!")

# Запуск программы
if __name__ == "__main__":
    main()
