# 5 глава - Задача 5
# Программа для вычисления суммы положительных чисел до первого отрицательного
sum_positive = 0

while True:
    number = int(input("Введите целое число: "))
    if number < 0:
        break
    sum_positive += number

print(f"Сумма положительных чисел до первого отрицательного: {sum_positive}")
