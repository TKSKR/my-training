# def summa(n):
#     if n == 0:
#         return  0
#     else:
#         return n + summa(n - 1)
# print(summa(4))
#
# def get_multiplied_digits(number):
#     str_number = str(number)
#     first = int(str_number[0])



def get_multiplied_digits(number):
    str_number = str(number)
    str_number = str_number.strip('0')

    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first
result = get_multiplied_digits(40203)
print(result)
result2 = get_multiplied_digits(402030000)
print(result2)
