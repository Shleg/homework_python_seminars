# Задача 26: Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
from functools import lru_cache


@lru_cache
def degree(a: int, b: int) -> int:
    if b == 1:
        return a
    return a * degree(a, b - 1)


print(degree(2, 8))
