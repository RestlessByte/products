# 6 глава - Задача 7
# Программа для сортировки списка из N элементов случайными целыми числами в интервале от 1 до 50 по возрастанию
import random

N = int(input("Введите количество элементов списка: "))
list_nums = [random.randint(1, 50) for _ in range(N)]

print(f"Исходный список: {list_nums}")
list_nums.sort()
print(f"Отсортированный список: {list_nums}")
