# 9 глава - Задача 18
def find_max_and_count(matrix):
    max_value = max(max(row) for row in matrix)
    count = sum(row.count(max_value) for row in matrix)
    return max_value, count

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [3, 3, 1],
        [2, 3, 1]
    ]
    max_value, count = find_max_and_count(matrix)
    print(f"Максимальный элемент: {max_value}, количество вхождений: {count}")
