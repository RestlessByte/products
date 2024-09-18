# 8 глава - Задача 22
# Программа для вычисления суммы элементов каждой строки матрицы 5x5
import random

A = [[random.randint(1, 40) for _ in range(5)] for _ in range(5)]
sums = [sum(row) for row in A]

print("Матрица:")
for row in A:
    print(row)
print("Суммы элементов строк:", sums)
