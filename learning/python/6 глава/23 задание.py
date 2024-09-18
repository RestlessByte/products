# 6 глава - Задача 23
# Программа для проверки наличия хотя бы одной пары совпадающих чисел в кортеже
tuple_A = tuple(map(int, input("Введите 10 целых чисел через пробел: ").split()))
has_duplicate = len(tuple_A) != len(set(tuple_A))

if has_duplicate:
    print("Есть хотя бы одна пара совпадающих чисел")
else:
    print("Совпадающих чисел нет")
