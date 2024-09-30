# 9 глава - Задача 6
def count_greater_in_matrix(matrix, znach):
    count = sum(1 for row in matrix for elem in row if elem > znach)
    return count

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    znach = 4
    count = count_greater_in_matrix(matrix, znach)
    print(f"Количество элементов больше {znach}: {count}")
