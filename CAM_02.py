import cv2
import os
import json

# Загрузка каскада Хаара для детекции лиц
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Захват видео с камеры
cap = cv2.VideoCapture(0)

# Папка для сохранения изображений лиц
faces_dir = 'faces'
if not os.path.exists(faces_dir):
    os.makedirs(faces_dir)

# Файл для хранения данных о людях
data_file = 'faces_data.json'
if os.path.exists(data_file):
    with open(data_file, 'r') as f:
        faces_data = json.load(f)
else:
    faces_data = {}

face_id = len(faces_data) + 1

# Переменная для хранения текущего обнаруженного лица
current_face = None

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Сохранение изображения лица
        face_img = frame[y:y+h, x:x+w]
        current_face = face_img  # Сохраняем текущее обнаруженное лицо

    # Отображение кадра с обнаруженными лицами
    cv2.imshow('Face Detection', frame)

    # Обработка нажатия клавиши
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):  # Выход по нажатию 'q'
        break
    elif key == ord('s') and current_face is not None:  # Сохранение лица по нажатию 's'
        face_filename = os.path.join(faces_dir, f'face_{face_id}.jpg')
        cv2.imwrite(face_filename, current_face)

        # Запрос имени человека через консоль (без блокировки видео)
        name = input(f"Введите имя для лица {face_id}: ")
        faces_data[face_id] = {'name': name, 'image_path': face_filename}
        face_id += 1

        # Сохранение данных в файл
        with open(data_file, 'w') as f:
            json.dump(faces_data, f)

        current_face = None  # Сбрасываем текущее лицо после сохранения

cap.release()
cv2.destroyAllWindows()