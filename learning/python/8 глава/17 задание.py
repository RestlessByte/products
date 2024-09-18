# 8 глава - Задача 17
# Программа для замены первого элемента каждой строки матрицы 5x5 на среднее арифметическое элементов строки
import random

A = [[random.randint(1, 20) for _ in range(5)] for _ in range(5)]

print("Исходная матрица:")
for row in A:
    print(row)

for i in range(5):
    avg = sum(A[i]) / 5
    A[i][0] = avg

print("Матрица после замены:")
for row in A:
    print(row)
