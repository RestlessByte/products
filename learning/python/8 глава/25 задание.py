# 8 глава - Задача 25
import random

def find_rightmost_min_element(matrix):
    rightmost_min_positions = []
    
    for row in matrix:
        min_val = min(row)
        min_pos = len(row) - 1 - row[::-1].index(min_val)
        rightmost_min_positions.append(min_pos)
    
    return rightmost_min_positions

# Создаем последовательность 5x5
matrix = [[random.randint(-20, 20) for _ in range(5)] for _ in range(5)]

# Выводим матрицу для наглядности
for row in matrix:
    print(row)

rightmost_min_positions = find_rightmost_min_element(matrix)
for i, pos in enumerate(rightmost_min_positions):
    print(f"Строка {i+1}, номер столбца с самым правым наименьшим элементом: {pos}")
