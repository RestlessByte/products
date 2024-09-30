# 6 глава - Задача 18
# Программа для нахождения наибольшего отрицательного элемента в списке
import random

N = int(input("Введите количество элементов списка: "))
list_nums = [random.randint(-15, 20) for _ in range(N)]
negative_nums = [num for num in list_nums if num < 0]

if negative_nums:
    max_negative = max(negative_nums)
    print(f"Наибольший отрицательный элемент: {max_negative}")
else:
    print("Отрицательных элементов нет.")
