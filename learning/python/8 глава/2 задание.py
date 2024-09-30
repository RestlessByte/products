# 8 глава - Задача 2
# Программа для нахождения суммы элементов матрицы 5x5, сумма индексов которых равна 4
import random

A = [[random.randint(1, 40) for _ in range(5)] for _ in range(5)]
sum_indices_4 = sum(A[i][j] for i in range(5) for j in range(5) if i + j == 4)

print("Матрица:")
for row in A:
    print(row)
print("Сумма элементов, сумма индексов которых равна 4:", sum_indices_4)
