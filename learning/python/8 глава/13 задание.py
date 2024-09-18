# 8 глава - Задача 13
# Программа для замены всех элементов матрицы 5x5 на нули и главной диагонали на ее номера
import random

A = [[random.randint(1, 40) for _ in range(5)] for _ in range(5)]

print("Исходная матрица:")
for row in A:
    print(row)

for i in range(5):
    for j in range(5):
        A[i][j] = i if i == j else 0

print("Преобразованная матрица:")
for row in A:
    print(row)
