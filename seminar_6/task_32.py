# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

from random import randint
from typing import List


def get_list(number: int) -> List[int]:
    return [randint(1, 10) for _ in range(number)]


num = int(input('Введите число элементов массива: '))
numbers = get_list(num)
print('Иcходный массив: ', numbers)
num_min = int(input('Введите минимум: '))
num_max = int(input('Введите максимум: '))

result = [i for i in range(len(numbers)) if num_min <= numbers[i] <= num_max]
print(*result)

