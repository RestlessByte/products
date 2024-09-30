# 8 глава - Задача 21
# Программа для вычисления количества положительных элементов на периметре и диагоналях матрицы 5x5
import random

A = [[random.randint(-20, 20) for _ in range(5)] for _ in range(5)]
positive_count = sum(A[i][j] > 0 for i in range(5) for j in range(5) if i == j or i + j == 4 or i == 0 or i == 4 or j == 0 or j == 4)

print("Матрица:")
for row in A:
    print(row)
print("Количество положительных элементов на периметре и диагоналях:", positive_count)
