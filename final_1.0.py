# Данные
grades = [[5,5,4,4,4,4,4],[5,5,5,3,4,3],[4,4,4,3,4],[2,2,4,4,5,5,5,3,3],[5,5,5,4,4,5,3]]
students = {"Борис", "Яков", "Антон", "Сергей", "Роман"}
# Приводим список студентов к упорядоченному списку
students_list = sorted(students)
# Создаём словарь для хранения средних баллов
mid_grades = {}
# Рассчитываем средний балл для каждого студента
for student, grade_list in zip(students_list, grades):
    mid_grades[student] = sum(grade_list) / len(grade_list)
# Выводим результат
print(mid_grades)