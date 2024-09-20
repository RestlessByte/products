# 8 глава - Задача 26
# Программа для вычисления среднего арифметического элементов матрицы 5x5, больших числа 20
import random

A = [[random.randint(1, 60) for _ in range(5)] for _ in range(5)]
elements_above_20 = [A[i][j] for i in range(5) for j in range(5) if A[i][j] > 20]
average_above_20 = sum(elements_above_20) / len(elements_above_20) if elements_above_20 else 0

print("Матрица:")
for row in A:
    print(row)
print(f"Среднее арифметическое элементов больше 20: {average_above_20}")
