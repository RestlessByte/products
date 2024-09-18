# 8 глава - Задача 1
# Программа для заполнения матрицы 5x5 случайными числами и нахождения номеров строк максимальных элементов каждого столбца
import random

A = [[random.randint(1, 40) for _ in range(5)] for _ in range(5)]
max_rows = [max(range(5), key=lambda i: A[i][j]) for j in range(5)]

print("Матрица:")
for row in A:
    print(row)
print("Номера строк максимальных элементов каждого столбца:", max_rows)
