# 8 глава - Задача 11
# Программа для упорядочивания строк матрицы 5x5: строки с нечетными индексами по убыванию, с четными - по возрастанию
import random

A = [[random.randint(1, 40) for _ in range(5)] for _ in range(5)]

print("Исходная матрица:")
for row in A:
    print(row)

for i in range(5):
    A[i].sort(reverse=(i % 2 != 0))

print("Преобразованная матрица:")
for row in A:
    print(row)
