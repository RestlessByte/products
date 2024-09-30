# 6 глава - Задача 22
# Программа для нахождения индекса последнего отрицательного элемента в кортеже
tuple_nums = tuple(map(int, input("Введите целые числа через пробел: ").split()))
last_negative_index = len(tuple_nums) - 1 - tuple_nums[::-1].index(next(filter(lambda x: x < 0, tuple_nums[::-1])))

print(f"Индекс последнего отрицательного элемента: {last_negative_index}")
