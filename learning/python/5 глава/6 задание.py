# 5 глава - Задача 6
# Программа для вычисления суммы всех ненулевых чисел
sum_non_zero = 0

while True:
    number = int(input("Введите целое число: "))
    if number == 0:
        break
    sum_non_zero += number

print(f"Сумма всех ненулевых чисел: {sum_non_zero}")
