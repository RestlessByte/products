# 9 глава - Задача 24
def find_max_indices(matrix):
    max_value = max(max(row) for row in matrix)
    indices = [(i, j) for i, row in enumerate(matrix) for j, val in enumerate(row) if val == max_value]
    return indices

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    indices = find_max_indices(matrix)
    print(f"Индексы максимальных элементов: {indices}")
