# 8 глава - Задача 12
# Программа для вычисления суммы наибольших значений в столбцах матрицы 5x5
import random

A = [[random.randint(1, 40) for _ in range(5)] for _ in range(5)]
max_elements = [max(A[i][j] for i in range(5)) for j in range(5)]
sum_max_elements = sum(max_elements)

print("Матрица:")
for row in A:
    print(row)
print("Список наибольших элементов в столбцах:", max_elements)
print("Сумма наибольших значений в столбцах:", sum_max_elements)
