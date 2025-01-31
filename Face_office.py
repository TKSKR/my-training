import cv2  # Импорт OpenCV
import face_recognition  # Распознавание лиц
import sqlite3  # Работа с базой данных
import os  # Работа с файловой системой
import datetime  # Работа с датами и временем
import pandas as pd  # Формирование отчетов

# Пути
DB_PATH = "employees.db"
KNOWN_FACES_DIR = "known_faces"


# Создание базы данных, если её нет
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS attendance (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT,
                        date TEXT,
                        time_in TEXT,
                        time_out TEXT)''')
    conn.commit()
    conn.close()


# Создание папки для лиц, если её нет
if not os.path.exists(KNOWN_FACES_DIR):
    os.makedirs(KNOWN_FACES_DIR)

# Загрузка известных лиц
known_face_encodings = []
known_face_names = []


def load_known_faces():
    known_face_encodings.clear()
    known_face_names.clear()
    for filename in os.listdir(KNOWN_FACES_DIR):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            image = face_recognition.load_image_file(os.path.join(KNOWN_FACES_DIR, filename))
            encoding = face_recognition.face_encodings(image)
            if encoding:
                known_face_encodings.append(encoding[0])
                known_face_names.append(os.path.splitext(filename)[0])


def scan_and_register_face():
    """Сканирование лица и добавление сотрудника в базу"""
    while True:
        cap = cv2.VideoCapture(0)

        while True:
            ret, frame = cap.read()
            if not ret:
                print("Ошибка: не удалось получить изображение с камеры.")
                break

            # Добавляем текст-инструкцию
            cv2.putText(frame, "Нажмите 's' для сохранения лица", (50, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

            cv2.imshow("Сканирование лица", frame)

            key = cv2.waitKey(1) & 0xFF
            if key == ord('s'):  # Нажмите 's' для сохранения
                name = input("Введите фамилию и имя сотрудника: ").strip()
                if not name:
                    print("Ошибка: имя не может быть пустым!")
                    continue  # Запрашиваем имя заново

                filename = os.path.join(KNOWN_FACES_DIR, f"{name}.jpg")
                cv2.imwrite(filename, frame)
                print(f"Лицо {name} сохранено.")
                break
            elif key == ord('q'):  # Нажмите 'q' для выхода
                print("Выход без сохранения.")
                cap.release()
                cv2.destroyAllWindows()
                return

        cap.release()
        cv2.destroyAllWindows()
        load_known_faces()  # Обновляем базу лиц


def recognize_and_track():
    cap = cv2.VideoCapture(0)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        for face_encoding, (top, right, bottom, left) in zip(face_encodings, face_locations):
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.5)
            name = "Неизвестный"
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]
                now = datetime.datetime.now()
                date = now.strftime("%Y-%m-%d")
                time = now.strftime("%H:%M:%S")

                cursor.execute("SELECT time_in FROM attendance WHERE name=? AND date=?", (name, date))
                record = cursor.fetchone()
                if not record:
                    cursor.execute("INSERT INTO attendance (name, date, time_in) VALUES (?, ?, ?)", (name, date, time))
                else:
                    cursor.execute("UPDATE attendance SET time_out=? WHERE name=? AND date=?", (time, name, date))
                conn.commit()

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

        cv2.imshow('Face Recognition', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    conn.close()
    cv2.destroyAllWindows()


def generate_report(month):
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM attendance", conn)
    conn.close()

    df['date'] = pd.to_datetime(df['date'])
    df['time_in'] = pd.to_datetime(df['time_in'])
    df['time_out'] = pd.to_datetime(df['time_out'])

    df['work_time'] = (df['time_out'] - df['time_in']).dt.total_seconds() / 3600
    df_month = df[df['date'].dt.month == month]
    df_summary = df_month.groupby('name')['work_time'].sum().reset_index()

    print("Отчёт о рабочем времени:")
    print(df_summary)


if __name__ == "__main__":
    init_db()
    load_known_faces()
    while True:
        action = input("Выберите действие: 1 - Сканирование лица, 2 - Распознавание и трекинг, 3 - Выход: ")
        if action == '1':
            scan_and_register_face()
        elif action == '2':
            recognize_and_track()
        elif action == '3':
            break
    generate_report(datetime.datetime.now().month)
