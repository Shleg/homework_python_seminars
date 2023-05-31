# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
# 5
# 1 2 3 4 5
# 3
# -> 1

from random import randint

num = int(input('Введите число элементов массива: '))

my_list = [randint(1, 100) for _ in range(num)]

print(*my_list)
num_x = int(input('Введите искомое число: '))

print(f"Число {num_x} встречается в массиве {my_list.count(num_x)} раз")