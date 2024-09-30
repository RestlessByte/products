# 8 глава - Задача 20
# Программа для упорядочивания столбцов матрицы 5x5 по убыванию
import random

A = [[random.randint(1, 40) for _ in range(5)] for _ in range(5)]

print("Исходная матрица:")
for row in A:
    print(row)

for j in range(5):
    column = sorted([A[i][j] for i in range(5)], reverse=True)
    for i in range(5):
        A[i][j] = column[i]

print("Матрица после упорядочивания столбцов по убыванию:")
for row in A:
    print(row)
