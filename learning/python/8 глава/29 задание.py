# 8 глава - Задача 29
# Программа для замены строк с хотя бы одним отрицательным элементом на нули в матрице 5x5
import random

A = [[random.randint(-15, 30) for _ in range(5)] for _ in range(5)]

print("Исходная матрица:")
for row in A:
    print(row)

for i in range(5):
    if any(A[i][j] < 0 for j in range(5)):
        A[i] = [0] * 5

print("Матрица после замены строк с отрицательными элементами:")
for row in A:
    print(row)
