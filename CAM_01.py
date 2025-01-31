import cv2  # Импорт библиотеки OpenCV
import os
import pickle

# Путь к файлу базы данных лиц
DATABASE_FILE = "face_database.pkl"


def load_face_database():
    """Загрузка базы данных лиц из файла."""
    if os.path.exists(DATABASE_FILE):
        with open(DATABASE_FILE, 'rb') as f:
            return pickle.load(f)
    return {}


def save_face_database(database):
    """Сохранение базы данных лиц в файл."""
    with open(DATABASE_FILE, 'wb') as f:
        pickle.dump(database, f)


def detect_faces():
    """
    Функция захватывает видеопоток с камеры, выполняет детекцию лиц с помощью каскада Хаара,
    сохраняет новые лица в базу данных с привязкой к ФИО и должности.
    При обнаружении известного лица на экране отображается имя, фамилия и должность сотрудника.
    """
    # Загрузка каскада Хаара для обнаружения лиц
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Открытие веб-камеры (индекс 0 указывает на основную камеру)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Ошибка: Не удалось открыть камеру")
        return

    # Загрузка существующей базы лиц
    face_database = load_face_database()

    while True:
        # Считываем кадр с камеры
        ret, frame = cap.read()
        if not ret:
            print("Ошибка: Не удалось получить кадр")
            break

        # Преобразование кадра в оттенки серого (ускоряет обработку)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Обнаружение лиц
        faces = face_cascade.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
        )

        # Обработка найденных лиц
        for (x, y, w, h) in faces:
            face_id = f"{x}_{y}_{w}_{h}"
            if face_id not in face_database:
                print("Найдено новое лицо. Введите данные сотрудника:")
                name = input("Введите имя: ")
                surname = input("Введите фамилию: ")
                position = input("Введите должность: ")
                face_database[face_id] = {"Имя": name, "Фамилия": surname, "Должность": position}
                save_face_database(face_database)  # Сохранение обновленной базы данных
                print("Лицо сохранено в базе данных.")
            else:
                # Получение данных сотрудника из базы
                person = face_database[face_id]
                label = f"{person['Фамилия']} {person['Имя']}, {person['Должность']}"
                cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

            # Отрисовка прямоугольников вокруг обнаруженных лиц
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Синий цвет, толщина 2 пикселя

        # Отображение кадра с выделенными лицами и подписями
        cv2.imshow('Система детекции лиц', frame)

        # Выход из программы по нажатию клавиши 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Освобождение ресурсов
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    detect_faces()  # Запуск функции детекции лиц
