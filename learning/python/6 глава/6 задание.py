# 6 глава - Задача 6
# Программа для определения процента нечетных элементов в списке
import random

N = int(input("Введите количество элементов списка: "))
list_nums = [random.randint(1, 40) for _ in range(N)]

odd_count = len([num for num in list_nums if num % 2 != 0])
percent_odd = (odd_count / N) * 100

print(f"Список: {list_nums}")
print(f"Процент нечетных элементов: {percent_odd:.2f}%")
