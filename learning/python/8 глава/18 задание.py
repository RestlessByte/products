# 8 глава - Задача 18
# Программа для определения номеров столбцов, среднее арифметическое которых меньше среднего арифметического всей матрицы
import random

A = [[random.randint(1, 40) for _ in range(5)] for _ in range(5)]

overall_avg = sum(sum(row) for row in A) / 25
cols = [j for j in range(5) if sum(A[i][j] for i in range(5)) / 5 < overall_avg]

print("Матрица:")
for row in A:
    print(row)
print("Номера столбцов с меньшим средним арифметическим:", cols)
