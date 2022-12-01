# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random
power_k = int(input('Введите натуральную степень: '))
equation = ''
for k in range(power_k, 1, -1):
    koefficient = random.randint(0,100)
    if koefficient != 0:
        equation += f'{koefficient} * x ** {k} + '

second_to_last_koef = random.randint(0,100)
if second_to_last_koef != 0:
    equation += f'{second_to_last_koef} * x + '
last_koef = random.randint(0,100)
if last_koef != 0:
    equation += str(random.randint(0,100))
equation += ' = 0'
print(equation)
