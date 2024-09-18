# 8 глава - Задача 9
# Программа для вывода половины матрицы 5x5 относительно главной диагонали
import random

A = [[random.randint(1, 40) for _ in range(5)] for _ in range(5)]

print("Матрица:")
for row in A:
    print(row)

print("Половина матрицы относительно главной диагонали:")
for i in range(5):
    for j in range(i + 1, 5):
        print(A[i][j], end=" ")
    print()
