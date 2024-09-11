# 6 глава - Задача 17
# Программа для умножения элементов списка на максимальный элемент
import random

N = int(input("Введите количество элементов списка: "))
list_nums = [random.uniform(1, 30) for _ in range(N)]
max_value = max(list_nums)

for i in range(len(list_nums)):
    if i % 2 == 0 and list_nums[i] < max_value:
        list_nums[i] *= max_value

print(f"Обновленный список: {list_nums}")
