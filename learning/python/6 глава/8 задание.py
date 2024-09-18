# 6 глава - Задача 8
# Программа для формирования списка: сначала отрицательные, затем положительные, и, наконец, нулевые элементы
list_A = list(map(int, input("Введите 10 чисел через пробел: ").split()))
negatives = [x for x in list_A if x < 0]
positives = [x for x in list_A if x > 0]
zeros = [x for x in list_A if x == 0]
result_list = negatives + positives + zeros

print(f"Преобразованный список: {result_list}")
