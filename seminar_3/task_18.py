# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
# 5
# 1 2 3 4 5
# 6
# -> 5

from random import randint

num = int(input('Введите число элементов массива: '))

my_list = [randint(1, 100) for _ in range(num)]

print(*my_list)
num_x = int(input('Введите искомое число: '))

my_dict = {abs(num_x - elem) : elem for elem in my_list }

nearest_num = my_dict[min(my_dict.keys())]

print(f"Ближайшее число в массиве равно: {nearest_num}")
