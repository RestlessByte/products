# 6 глава - Задача 25
# Программа для нахождения максимального и минимального элементов списка и вычисления их разности
import random

N = int(input("Введите количество элементов списка: "))
list_nums = [random.randint(1, 50) for _ in range(N)]

max_value = max(list_nums)
min_value = min(list_nums)
difference = max_value - min_value

print(f"Список: {list_nums}")
print(f"Максимальный элемент: {max_value}, Минимальный элемент: {min_value}")
print(f"Разность между максимальным и минимальным элементами: {difference}")
