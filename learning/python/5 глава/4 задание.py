# 5 глава - Задача 4
# Программа для нахождения суммы положительных и отрицательных чисел в последовательности
N = int(input("Введите количество элементов последовательности: "))
positive_sum = 0
negative_sum = 0
i = 1

while i <= N:
    number = float(input(f"Введите число {i}: "))
    if number > 0:
        positive_sum += number
    elif number < 0:
        negative_sum += number
    i += 1

print(f"Сумма положительных чисел: {positive_sum}")
print(f"Сумма отрицательных чисел: {negative_sum}")
