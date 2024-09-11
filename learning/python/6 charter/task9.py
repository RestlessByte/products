# 6 глава - Задача 9
# Программа для нахождения максимального элемента списка, его номера и замены с первым элементом
import random

N = int(input("Введите количество элементов списка: "))
list_nums = [random.randint(1, 30) for _ in range(N)]

print(f"Исходный список: {list_nums}")
max_index = list_nums.index(max(list_nums))
list_nums[0], list_nums[max_index] = list_nums[max_index], list_nums[0]
print(f"Измененный список: {list_nums}")
