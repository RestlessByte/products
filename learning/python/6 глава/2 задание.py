# 6 глава - Задача 2
# Программа для формирования двух списков: четных и нечетных чисел из исходного списка
list_nums = list(map(int, input("Введите целые числа через пробел: ").split()))
even_nums = [num for num in list_nums if num % 2 == 0]
odd_nums = [num for num in list_nums if num % 2 != 0]

print(f"Список четных чисел: {even_nums}")
print(f"Список нечетных чисел: {odd_nums}")
