# 6 глава - Задача 19
# Программа для подсчета элементов, значения которых находятся в диапазоне от A до B
import random

N = int(input("Введите количество элементов списка: "))
A = int(input("Введите начало диапазона A: "))
B = int(input("Введите конец диапазона B: "))
list_nums = [random.randint(1, 50) for _ in range(N)]

count_in_range = len([num for num in list_nums if A <= num <= B])

print(f"Список: {list_nums}")
print(f"Количество элементов в диапазоне от {A} до {B}: {count_in_range}")
