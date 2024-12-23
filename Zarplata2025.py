from datetime import datetime

print(f"Сейчас часов: {datetime.now().hour}, Минут: {datetime.now().minute}, Дата: {datetime.now().day},Месяц: {datetime.now().month}, Год: {datetime.now().year}")

from time import sleep
#import emoji
print('Привет! Я робот, с которым можно обсудить повышение вашей зарплаты.')
employee_name = ["Сергей", "Света"]
employee_surname = ["Коротков", "Короткова", "Кочетков"]
employee_post = ["Директор", "Менеджер"]

while True:
    name = input("Как Вас зовут?: ")
    name = name.lower()
    if name in [employee_name.lower() for employee_name in employee_name]:
      print("Отлично!")
      break
    elif name in [employee_surname.lower() for employee_surname in employee_surname]:
      print("Вы ввели фамилию. А я спрашиваю имя.")
    else:
        print("Сотрудника с таким именем нет в нашей организации! Попробуйие еще раз")

while True:
    surname = input("Как Ваша фамилия?: ")
    surname = surname.lower()
    if surname in [employee_surname.lower() for employee_surname in employee_surname]:
        print("Есть такая фамилия! Нашел Вас!")
        break
    elif surname in [employee_name.lower() for employee_name in employee_name]:
        print("Вы ввели имя, а я просил фамилию.")
    else:
        print("Сотрудника с такой фамилией нет в нашей организации. Попробуйте еще раз.")
while True:
    post = input("На какой должности вы работаете?: ")
    post = post.lower()
    if post in [employee_post.lower() for employee_post in employee_post]:
        print("Отлично! Есть такой сотрудник на такой должности")
        break
    else:
        print("Введите должность еще раз одним словом. Например 'менеджер'")

print("Оооооо это тот, который ЛУЧШИЙ В МИРЕ", post.upper(), name.upper(), surname.upper(),'? \U0001F60A')
print("Наслышан о Вас, наслышан. И не  могу сказать что только хорошее.")
print("Скорее наоборот. Ходят, знаете ли, некие слухи....")
yes = "да"
no = "нет"
while True:
    rumors = input("Рассказать? (да/нет): ")
    if rumors.lower() == yes:
        print('Хорошо, расскажу как нибудь. Но двайте сначала о деле')
        print("Как говориться сначала про деньги, потом про стулья.")
        break
    elif rumors.lower() == no:
        print("Ну как хотите. А я б посплетничал. Ладно, посплетничаю с кем нибудь еще.")
        break
    else:
        print('Ответьте только "да" или "нет')
year = 2024
while True:
    try:
        salary_2024 = int(input("Какой оклад у Вас был в 2024 году?: "))
        if salary_2024 < 0:
            print("Ошибка: число должно быть положительным. Попробуйте снова.")
        else:
            break
    except ValueError:
        print("Ошибка: введите корректное число.")
while True:
    try:
        salary_2025 = int(input("Какой желаемый оклад Вы хотели бы в 2025 году?: "))
        if salary_2025 < 0:
            print("Ошибка: число должно быть положительным. Попробуйте снова.")
        else:
            break
    except ValueError:
        print("Ошибка!!! Введите корректное число!")
salary_2024_2025 = salary_2025 - salary_2024
print("Это ж больше на целых", salary_2024_2025, "рублей !!!")
while True:
    try:
        work_year = int(input("В каком году Вы пришли к нам работать?: "))
        if work_year > 2025:
            print("Вы не могли устроиться в будущем! Введите корректную цифры!")
        elif work_year < 2004:
                print("Вы не могли устроится ранее 2004 года! Введите корректные цифры!")
        else:
            break
    except ValueError:
        print("Введите корректные цифры!")
work_experience = year - work_year
print("Т.е. Вы работаете у нас уже почти......ммммммм ")
from time import sleep
sleep(4)
print("ууууууффф, четыре секунды считал")
print("Получается уже", work_experience, "лет. Хм.....")
print("В общем я проанализировал полученную информацию, и боюсь что смогу поднять вам оклад всего на 500 руб, т.е. на один штраф.")

print("Если хотите больше - обратитесь к Сергею Анатольевичу.")
while True:
    user_input = input('Вы довольны? (да/нет): ')
    if user_input.lower() == 'да':
        print('Ну хорошо, коли так. Замолвлю за Вас словечко перед С.А.. Спасибо и всего хорошего!')
        break
    elif user_input.lower() == 'нет':
        print('Ну что ж, нет так нет. Доложу руководству о Вашей беспредельной жадности.')
        print("Не могу сказать что рад знакомству. До свидания")
        break
    else:
        print('Ответьте "да" или "нет"')
input('')


