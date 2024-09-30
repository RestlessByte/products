# 8 глава - Задача 8
# Программа для вывода главной и побочной диагоналей матрицы 5x5
import random

A = [[random.randint(1, 50) for _ in range(5)] for _ in range(5)]
main_diagonal = [A[i][i] for i in range(5)]
secondary_diagonal = [A[i][4 - i] for i in range(5)]

print("Матрица:")
for row in A:
    print(row)
print("Главная диагональ:", main_diagonal)
print("Побочная диагональ:", secondary_diagonal)
