# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0
import random


def input_int(text: str, error: str) -> int:
    while True:
        try:
            number = int(input(text))
            return number
        except:
            print(error)


def create_polinominal(power, min, max):
    equation = ''
    for k in range(power, 1, -1):
        koefficient = random.randint(min, max)
        if koefficient != 0:
            equation += f'{koefficient} * x ** {k} + '

    second_to_last_koef = random.randint(min, max)
    if second_to_last_koef != 0:
        equation += f'{second_to_last_koef} * x + '
    last_koef = random.randint(min, max)
    if last_koef != 0:
        equation += str(random.randint(min, max))
    equation += ' = 0'
    return equation


power_k = input_int('Введите натуральную степень: ', 'Это должно быть целое число, попробуйте еще раз')

first_equitation = create_polinominal(power_k, 0, 100)
second_equitation = create_polinominal(power_k, 0, 100)
print(first_equitation)
print(second_equitation)
