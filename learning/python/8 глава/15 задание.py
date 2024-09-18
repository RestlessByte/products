# 8 глава - Задача 15
# Программа для перемножения двух матриц 5x5
import random

A = [[random.randint(1, 10) for _ in range(5)] for _ in range(5)]
B = [[random.randint(1, 10) for _ in range(5)] for _ in range(5)]
C = [[sum(A[i][k] * B[k][j] for k in range(5)) for j in range(5)] for i in range(5)]

print("Матрица A:")
for row in A:
    print(row)

print("Матрица B:")
for row in B:
    print(row)

print("Результат перемножения A и B (матрица C):")
for row in C:
    print(row)
