# 6 глава - Задача 14
# Программа для формирования двух списков: номеров положительных и отрицательных элементов
list_A = list(map(int, input("Введите 10 чисел через пробел: ").split()))
positive_indices = [i for i in range(len(list_A)) if list_A[i] > 0]
negative_indices = [i for i in range(len(list_A)) if list_A[i] < 0]

print(f"Номера положительных элементов: {positive_indices}")
print(f"Номера отрицательных элементов: {negative_indices}")
