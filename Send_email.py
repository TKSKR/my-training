def send_email(message, recipient, *, sender = "urban@gmail.com"):
  #print(message, recipient, sender)
# message - сообщение
# recipient - получатель
# sender - отправитель
  if '@' not in recipient or not recipient.endswith(('.com', '.ru', '.net')):
    # если "@" нет в получателе или в конце строки с получателем нет .com', '.ru', '.net'
    # Метод endswith (перевод "заканчивается словами") в Python проверяет окончание строки
    # и возвращает значение True, если строка заканчивается указанным суффиксом,
    # в противном случае — False.
    print(f"Адрес получателя указан некорректно. Нельзя отправить письмо с адреса {sender} на адрес {recipient}.")
  elif '@' not in sender or not sender.endswith(('.com', '.ru', '.net')):
    # если "@" нет в отправителе или в конце строки с отправителем нет .com', '.ru', '.net'
    print(f"Адрес отправителя указан некорректно. Нельзя отправить письмо с адреса {sender} на адрес {recipient}.")
    return
  if recipient == sender:
    # если адрес отправителя и получателя совпадают
    print("Нельзя отправить письмо самому себе!")
    return
  if sender == "urban@gmail.com":
      print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
  else:
      print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ!!! Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
send_email('Привет!!!', 'kor.ser@mail.ru')
send_email('Привет!!!', 'kor.ser@mail.ru', sender ='urdan@mil.su')
send_email('Привет!!!', 'kor.ser@mail.su', sender='urdan@mil.su')
send_email('Привет!!!', 'kor.ser@mail.su', sender='urban@mail.ru')
send_email('Привет!!!', 'kor.ser@mail.ru', sender='urban@mail.ru')





