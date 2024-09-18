# 8 глава - Задача 6
# Программа для вычисления среднего арифметического элементов строки матрицы 5x5 в заданном диапазоне
import random

A = [[random.randint(1, 40) for _ in range(5)] for _ in range(5)]
lower_bound = int(input("Введите нижнюю границу диапазона: "))
upper_bound = int(input("Введите верхнюю границу диапазона: "))

averages = []
for row in A:
    filtered_elements = [x for x in row if lower_bound < x < upper_bound]
    avg = sum(filtered_elements) / len(filtered_elements) if filtered_elements else 0
    averages.append(avg)

print("Матрица:")
for row in A:
    print(row)
print("Средние арифметические для каждой строки:", averages)
