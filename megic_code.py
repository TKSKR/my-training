def get_magic_code(n):
  result = ""
  used_pairs = set()
  for i in range(1, 21):
      for j in range(i + 1, 21):
          if (i + j) != 0 and n % (i + j) == 0:
                pair = (i, j)
                if pair not in used_pairs:
                   result += str(i) + str(j)
                   used_pairs.add(pair)
  return result
while True:
    try:
       user_input = int(input("Введите число от 3 до 20: "))
       if 3 <= user_input <= 20:
           break
       else:
          print("Введенное число не соответствует диапазону от 3 до 20.")
    except ValueError:
        print("Некорректный ввод. Введите целое число от 3 до 20.")
result = get_magic_code(user_input)
print(f"Код для числа {user_input}: {result}")