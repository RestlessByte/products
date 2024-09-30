# 8 глава - Задача 30
# Программа для нахождения количества, суммы и среднего арифметического отрицательных чисел матрицы 5x5
import random

A = [[random.randint(-20, 40) for _ in range(5)] for _ in range(5)]
negative_numbers = [A[i][j] for i in range(5) for j in range(5) if A[i][j] < 0]

negative_count = len(negative_numbers)
negative_sum = sum(negative_numbers)
negative_avg = negative_sum / negative_count if negative_count > 0 else 0

print("Матрица:")
for row in A:
    print(row)
print(f"Количество отрицательных чисел: {negative_count}")
print(f"Сумма отрицательных чисел: {negative_sum}")
print(f"Среднее арифметическое отрицательных чисел: {negative_avg:.2f}")
