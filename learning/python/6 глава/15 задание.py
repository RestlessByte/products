# 6 глава - Задача 15
# Программа для вычисления среднего арифметического квадратов положительных элементов списка
import random

N = int(input("Введите количество элементов списка: "))
list_nums = [random.randint(-20, 40) for _ in range(N)]

positive_squares = [num ** 2 for num in list_nums if num > 0]
if positive_squares:
    average_square = sum(positive_squares) / len(positive_squares)
    print(f"Среднее арифметическое квадратов положительных элементов: {average_square:.2f}")
else:
    print("Нет положительных элементов.")
