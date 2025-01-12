def single_root_words(root_word, *other_words):
    same_words = []
    for word in other_words:
        if root_word.lower() in word.lower():
            same_words.append(word)
    return same_words
result1 = single_root_words("Цвет", "цветной", "ЦветЫ", "ветка", "работа", "Самоцвет")
result2 = single_root_words("Век", "человек", "вековой", "верный", "Велосипед")
print(result1)
print(result2)
#
# def test_func(*params):
#     print(params)
#     print("ТИП:", type(params))
#     print("АРГУМЕНТ:", params)
#
# test_func(1, 2, 3, 4)
#
# def summator(*values):
#     s = 0
#     for i in values:
#         s +=i
#     return s
# print(summator(1,2,3,4))
#
# def summator(txt, *values, type = 'sum'):
#     s = 0
#     for i in values:
#         s +=i
#     return f'{txt} {s} {type}'
# print(summator("СУММА ЧИСЕЛ:",2,3,4, type = 'summator'))
#
# def info_peeple(value, *types, names_author="SERG", **values):
#     print('ТИП:', type(values))
#     print('Аргумент:', values)
#     for key, value in values.items():
#         print(key, value)
#     print(types)
# info_peeple('Пример использования параметров всех типов', 2,3,4, names_author='Sergei', name='SERG', course='PYTHON')
#
# def my_sum(n, *args, txt="Сумма чисел"):
#     s = 0
#     for i in range(len(args)):
#         s += args[i] ** n
#     print(txt +':', s)
# my_sum(1, 1, 2, 3, 4, 5)
# my_sum(2, 2, 3, 4, 5, txt = "Сумма квадратов")
# my_sum(3, 2, 3, 4, 5, txt="Сумма кубов")
#
#
#
#
