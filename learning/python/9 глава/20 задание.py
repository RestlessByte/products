# 9 глава - Задача 20
def multiply_sequences(A, B):
    result = []
    for i in range(len(A)):
        result.append([A[i][j] * B[i][j] for j in range(len(A[i]))])
    return result

if __name__ == "__main__":
    A = [
        [1, 2],
        [3, 4]
    ]
    B = [
        [5, 6],
        [7, 8]
    ]
    result = multiply_sequences(A, B)
    for row in result:
        print(row)
