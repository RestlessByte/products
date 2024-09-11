# 6 глава - Задача 12
# Программа для определения наличия серий знакочередующихся чисел в списке
import random

N = int(input("Введите количество элементов списка: "))
list_nums = [random.randint(-30, 50) for _ in range(N)]
series_count = 0
is_in_series = False

print(f"Список: {list_nums}")

for i in range(1, len(list_nums)):
    if list_nums[i] * list_nums[i - 1] < 0:
        if not is_in_series:
            series_count += 1
            is_in_series = True
    else:
        is_in_series = False

print(f"Количество серий знакочередующихся чисел: {series_count}")
