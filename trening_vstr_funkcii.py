salary = [2300, 1800.805353,5000,1235.587868, 7500.12978078]
print(len(salary))
print(round(sum(salary), 2), len(salary))
print(round(sum(salary)/len(salary), 2), 'Средняя зарплата в компании')
print(round(max(salary), 2), 'максимальная зарплата')
print(round(min(salary), 2), 'минимальная зарплата')

names  = ["Сергей", "Света", "Кирилл", "Даниил"]
zipped = dict(zip(names, salary))
print(zipped)
print(round(zipped["Сергей"], 2), "-зарплата Сергея")
print(round(zipped["Света"], 2), "-зарплата Светы" )