# 6 глава - Задача 16
# Программа для обмена соседних элементов, стоящих на четных и нечетных местах
tuple_nums = tuple(map(int, input("Введите целые числа через пробел: ").split()))
new_tuple = list(tuple_nums)

for i in range(1, len(new_tuple), 2):
    new_tuple[i - 1], new_tuple[i] = new_tuple[i], new_tuple[i - 1]

new_tuple = tuple(new_tuple)
print(f"Измененный кортеж: {new_tuple}")
