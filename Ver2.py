from collections.abc import async_generator

print(5 <= 10) # boolian
print(10 // 2) # целочисленное деление
print(5 != 5) # не равно
print(5 > 5 and 5 == 5)
print(5 > 5 or 5 == 5)
print(type(int('5')))
print("1st program")
print(9 ** 0.5 * 5)
print("2nd program")
print(9.99 > 9.98 or 1000 != 1000.1)
print("3rd program")
print(2 * 2 + 2)
print(2 * (2 + 2))
print((2 * 2 + 2) == (2* (2 + 2)))
print(6 == 8)
print("4th program")
print('123.456')
print(float('123.456'))
print(type(float('123.456')))
print(10 * (float('123.456')))
print((float('123.456')) * 10)
name = 'ARISENTA'
print(name, type (name))
name = 5
print(name, type (name))
name = 5.5
print(name, type (name))
name = [1, 2, 3, 4, 5]
print(name, type (name))
age = 100
new_age = 100
print(age + new_age)

name = 'SERGEI'
print('KOROTKOV ' + name)
print(name[0] + name[2] + name[3])
name = 'SERGEI'
print(name[0:4])
date_of_birth = '1974'
print(date_of_birth)
amount_of_homework = 12
number_of_hours_spent = 15
course_name = 'Python'
time_for_one_task = number_of_hours_spent / amount_of_homework
print('Курс', course_name,',', 'всего',amount_of_homework, 'домашних', 'заданий', ',','затрачено', number_of_hours_spent, 'часов', ',','среднее', 'время', 'выполнения', time_for_one_task, 'часа')