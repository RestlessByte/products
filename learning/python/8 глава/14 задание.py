# 8 глава - Задача 14
# Программа для обмена второй и четвертой строки в матрице 5x5
import random

A = [[random.randint(1, 40) for _ in range(5)] for _ in range(5)]

print("Исходная матрица:")
for row in A:
    print(row)

A[1], A[3] = A[3], A[1]

print("Матрица после обмена второй и четвертой строки:")
for row in A:
    print(row)
