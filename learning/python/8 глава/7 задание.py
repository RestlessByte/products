# 8 глава - Задача 7
# Программа для создания списков элементов выше и ниже главной диагонали матрицы 5x5
import random

A = [[random.randint(1, 20) for _ in range(5)] for _ in range(5)]
above_diagonal = [A[i][j] for i in range(5) for j in range(i, 5)]
below_diagonal = [A[i][j] for i in range(1, 5) for j in range(i)]

print("Матрица:")
for row in A:
    print(row)
print("Элементы на и выше главной диагонали:", above_diagonal)
print("Элементы ниже главной диагонали:", below_diagonal)
