example = "Экранизация"
print(example[0])
print(example[-1])
half_index = len(example) // 2
second_half = example[half_index:]
print(second_half)
revers_string = example[::-1]
print(revers_string)
every_second_char = example[1::2]
print(every_second_char)

# Задаем строку
example = 'Топинамбур'

# 1. Вывод первого символа строки
print(example[0])  # Т

# 2. Вывод последнего символа строки (с использованием отрицательного индекса)
print(example[-1])  # р

# 3. Вывод второй половины строки
half_index = len(example) // 2  # Находим индекс середины строки
second_half = example[half_index:]  # Берем строку с середины до конца
print(second_half)  # амбур

# 4. Вывод строки наоборот
reversed_string = example[::-1]  # Переворачиваем строку
print(reversed_string)  # рубманипоТ

# 5. Вывод каждого второго символа строки
every_second_char = example[1::2]  # Берем каждый второй символ, начиная с индекса 1
print(every_second_char)  # оиабр
