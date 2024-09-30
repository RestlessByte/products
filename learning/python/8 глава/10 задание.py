# 8 глава - Задача 10
# Программа для нахождения сумм элементов на диагоналях, параллельных побочной и главной диагоналям
import random

A = [[random.randint(1, 40) for _ in range(5)] for _ in range(5)]

sum_parallel_secondary = sum(A[i][4 - i + 1] for i in range(4))
sum_parallel_main = sum(A[i + 1][i] for i in range(4))

print("Матрица:")
for row in A:
    print(row)
print("Сумма элементов на диагонали, параллельной побочной:", sum_parallel_secondary)
print("Сумма элементов на диагонали, параллельной главной:", sum_parallel_main)
