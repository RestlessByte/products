# 8 глава - Задача 24
import random

def find_max_above_diagonal_min_below_diagonal(matrix):
    max_above = float("-inf")
    min_below = float("inf")

    for i in range(5):
        for j in range(5):
            if i < j:  # Элементы выше главной диагонали
                max_above = max(max_above, matrix[i][j])
            elif i > j:  # Элементы ниже главной диагонали
                min_below = min(min_below, matrix[i][j])

    return max_above, min_below

# Создаем последовательность 5x5
matrix = [[random.randint(1, 50) for _ in range(5)] for _ in range(5)]

# Выводим матрицу для наглядности
for row in matrix:
    print(row)

max_above, min_below = find_max_above_diagonal_min_below_diagonal(matrix)
print(f"Максимальный элемент выше главной диагонали: {max_above}")
print(f"Минимальный элемент ниже главной диагонали: {min_below}")
