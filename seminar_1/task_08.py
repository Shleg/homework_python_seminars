# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить num долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
#
# *Пример:*
#
# 3 2 4 -> yes
# 3 2 1 -> no
def can_divide(height: int, width: int, num: int) -> bool:
    if (num % height == 0 or num % width == 0) and num < height * width:
        return 'YES'
    else:
        return 'NO'

height_choco = int(input('Введите кол-во долек по вертикали: '))
width_choco = int(input('Введите кол-во долек по горизонтали: '))

number_slices = int(input('Введите сколько долек надо отломить: '))

result = can_divide(height_choco, width_choco, number_slices)

print(f"{height_choco} {width_choco} {number_slices} -> {result} ")