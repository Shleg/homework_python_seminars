# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
#
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |
print('Option 1: Integer division and remainder')
num = int(input('Enter a three-digit number: '))

result = num // 100 + num % 100 // 10 + num % 10

print(result)

print('\nOption 2: Loop')
num = input('Enter a three-digit number: ')
result_2 = 0

for elem in num:
    result_2 += int(elem)

print(result_2)

print('\nOption 2: Slices')
num = input('Enter a three-digit number: ')

result_3 = int(num[:1]) + int(num[1:2]) + int(num[-1])

print(result_3)

