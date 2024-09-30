# 9 глава - Задача 21
def sum_less_than_in_matrix(matrix, Znach):
    total_sum = sum(elem for row in matrix for elem in row if elem < Znach)
    return total_sum

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    Znach = 5
    total_sum = sum_less_than_in_matrix(matrix, Znach)
    print(f"Сумма значений меньше {Znach}: {total_sum}")
