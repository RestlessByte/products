# 8 глава - Задача 16
# Программа для вычисления сумм элементов выше и ниже главной диагонали матрицы 5x5
import random

A = [[random.randint(1, 40) for _ in range(5)] for _ in range(5)]
sum_above = sum(A[i][j] for i in range(5) for j in range(i))
sum_below = sum(A[i][j] for i in range(5) for j in range(i + 1, 5))

print("Матрица:")
for row in A:
    print(row)
print("Сумма элементов выше главной диагонали:", sum_above)
print("Сумма элементов ниже главной диагонали:", sum_below)
