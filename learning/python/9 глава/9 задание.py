# 9 глава - Задача 9
def replace_elements(matrix, znach1, znach2):
    return [[znach2 if elem != znach1 else elem for elem in row] for row in matrix]

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 2, 6],
        [7, 8, 9]
    ]
    znach1 = 2
    znach2 = 0
    result = replace_elements(matrix, znach1, znach2)
    for row in result:
        print(row)
