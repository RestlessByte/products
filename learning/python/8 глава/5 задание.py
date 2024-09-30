# 8 глава - Задача 5
# Программа для вычисления среднего арифметического положительных элементов и количества нулей в матрице 5x5
import random

A = [[random.randint(-15, 40) for _ in range(5)] for _ in range(5)]
positive_elements = [A[i][j] for i in range(5) for j in range(5) if A[i][j] > 0]
zeros_count = sum(1 for i in range(5) for j in range(5) if A[i][j] == 0)

average_positive = sum(positive_elements) / len(positive_elements) if positive_elements else 0

print("Матрица:")
for row in A:
    print(row)
print("Среднее арифметическое положительных элементов:", average_positive)
print("Количество нулей:", zeros_count)
