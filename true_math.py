# import math
# def divide(first, second):
#     if second == 0:
#         return math.inf
#     return first / second
# print(divide(56, 8))
# print(divide(234, 0))
import translators as ts

result = ts.translate_text("Как дела?", translator="deepl", from_language="ru", to_language="en")

print(result)  # Вывод: How are you?