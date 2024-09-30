# 9 глава - Задача 25
def sum_negative_in_rows(matrix):
    return [sum(x for x in row if x < 0) for row in matrix]

if __name__ == "__main__":
    matrix = [
        [-1, 2, -3],
        [4, -5, 6],
        [-7, 8, 9]
    ]
    result = sum_negative_in_rows(matrix)
    print(f"Сумма отрицательных элементов в каждой строке: {result}")
