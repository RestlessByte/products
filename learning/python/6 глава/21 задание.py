# Программа для замены нулями элементов между максимальным и минимальным значениями
import random

# Ввод количества элементов
N = int(input("Введите количество элементов списка: "))

# Заполнение списка случайными числами
list_nums = [random.randint(1, 30) for _ in range(N)]

# Поиск индексов максимального и минимального значений
max_index = list_nums.index(max(list_nums))
min_index = list_nums.index(min(list_nums))

# Заменяем элементы между максимальным и минимальным значениями на нули
if min_index < max_index:
    list_nums[min_index + 1:max_index] = [0] * (max_index - min_index - 1)
else:
    list_nums[max_index + 1:min_index] = [0] * (min_index - max_index - 1)

# Вывод обновленного списка
print(f"Обновленный список: {list_nums}")
