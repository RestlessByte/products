# 9 глава - Задача 16
def delete_row(matrix, N_st):
    return matrix[:N_st] + matrix[N_st+1:]

if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    N_st = 1
    result = delete_row(matrix, N_st)
    for row in result:
        print(row)
