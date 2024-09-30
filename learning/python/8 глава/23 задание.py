# 8 глава - Задача 23
# Программа для вычисления суммы максимальных значений в строках матрицы 5x5
import random

A = [[random.randint(1, 40) for _ in range(5)] for _ in range(5)]
max_elements = [max(row) for row in A]
sum_max_elements = sum(max_elements)

print("Матрица:")
for row in A:
    print(row)
print("Список максимальных элементов в строках:", max_elements)
print("Сумма максимальных значений в строках:", sum_max_elements)
