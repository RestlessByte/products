# 6 глава - Задача 5
# Программа для создания списка из N элементов случайными целыми числами в интервале от -20 до 40, изменение элементов списка
import random

N = int(input("Введите количество элементов списка: "))
list_nums = [random.randint(-20, 40) for _ in range(N)]

print(f"Исходный список: {list_nums}")

for i in range(len(list_nums)):
    if list_nums[i] > 0:
        list_nums[i] /= 2
    else:
        list_nums[i] = i

print(f"Измененный список: {list_nums}")
