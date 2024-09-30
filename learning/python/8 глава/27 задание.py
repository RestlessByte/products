# 8 глава - Задача 27
# Программа для поворота матрицы 5x5 на 90 градусов по часовой стрелке
import random

A = [[random.randint(1, 30) for _ in range(5)] for _ in range(5)]
rotated_A = [[A[4 - j][i] for j in range(5)] for i in range(5)]

print("Исходная матрица:")
for row in A:
    print(row)

print("Матрица после поворота на 90 градусов:")
for row in rotated_A:
    print(row)
