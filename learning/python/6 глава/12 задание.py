# 6 глава - Задача 12
# Программа для определения наличия серий знакочередующихся чисел в списке
import random

N = int(input("Введите количество элементов списка: "))
list_nums = [random.randint(-30, 50) for _ in range(N)]
series_count = 0
in_series = False

print(f"Список: {list_nums}")

# Перебираем список, начиная со второго элемента
for i in range(1, len(list_nums)):
    # Проверяем на чередование знаков
    if (list_nums[i] < 0 and list_nums[i - 1] >= 0) or (list_nums[i] > 0 and list_nums[i - 1] < 0):
        # Если обнаружено чередование, увеличиваем счетчик серий
        if not in_series:
            series_count += 1
            in_series = True
    else:
        # Если чередования нет, выходим из текущей серии
        in_series = False1

# Учитываем завершение последней серии
if in_series:
    series_count += 1

print(f"Количество серий знакочередующихся чисел: {series_count}")
