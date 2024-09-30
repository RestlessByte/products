# 9 глава - Задача 8
def multiply_matrix(matrix, chislo):
    return [[elem * chislo for elem in row] for row in matrix]

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    chislo = 2
    result = multiply_matrix(matrix, chislo)
    for row in result:
        print(row)
