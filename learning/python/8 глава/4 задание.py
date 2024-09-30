# 8 глава - Задача 4
# Программа для нахождения всех четных элементов матрицы 5x5
import random

A = [[random.randint(1, 80) for _ in range(5)] for _ in range(5)]
even_elements = [A[i][j] for i in range(5) for j in range(5) if A[i][j] % 2 == 0]

print("Матрица:")
for row in A:
    print(row)
print("Четные элементы:", even_elements)
