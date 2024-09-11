# 6 глава - Задача 4
# Программа для нахождения максимального и минимального элементов среди положительных нечетных элементов целочисленного кортежа A(10)
import random

tuple_nums = tuple(random.randint(-20, 50) for _ in range(10))
odd_positive = [num for num in tuple_nums if num > 0 and num % 2 != 0]

if odd_positive:
    max_val = max(odd_positive)
    min_val = min(odd_positive)
    print(f"Максимальный положительный нечетный элемент: {max_val}")
    print(f"Минимальный положительный нечетный элемент: {min_val}")
else:
    print("Нет положительных нечетных элементов.")
