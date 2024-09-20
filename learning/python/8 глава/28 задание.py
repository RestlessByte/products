# 8 глава - Задача 28
# Программа для проверки наличия отрицательных чисел ниже главной диагонали матрицы 5x5
import random

A = [[random.randint(1, 40) if i <= j else random.randint(-15, 0) for j in range(5)] for i in range(5)]
negatives_below = any(A[i][j] < 0 for i in range(1, 5) for j in range(i))

print("Матрица:")
for row in A:
    print(row)
print("Есть ли отрицательные числа ниже главной диагонали?", "Да" if negatives_below else "Нет")
