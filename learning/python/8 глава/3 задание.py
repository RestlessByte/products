# 8 глава - Задача 3
# Программа для нахождения наибольшего элемента побочной диагонали матрицы 5x5
import random

A = [[random.randint(1, 40) for _ in range(5)] for _ in range(5)]
max_secondary_diag = max(A[i][4 - i] for i in range(5))

print("Матрица:")
for row in A:
    print(row)
print("Наибольший элемент побочной диагонали:", max_secondary_diag)
