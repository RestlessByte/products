# 8 глава - Задача 19
# Программа для проверки, является ли введенная пользователем матрица 5x5 единичной
A = []
print("Введите элементы матрицы 5x5:")
for i in range(5):
    A.append([int(x) for x in input().split()])

is_identity = all(A[i][j] == (1 if i == j else 0) for i in range(5) for j in range(5))

print("Матрица:")
for row in A:
    print(row)
print("Матрица является единичной" if is_identity else "Матрица не является единичной")
