# 6 глава - Задача 3
# Программа для вычисления среднего арифметического элементов кортежа, удовлетворяющих условию abs(korteg[i]) > C
tuple_nums = tuple(map(int, input("Введите элементы кортежа через пробел: ").split()))
C = float(input("Введите значение C: "))
filtered_elements = [num for num in tuple_nums if abs(num) > C]

if filtered_elements:
    avg = sum(filtered_elements) / len(filtered_elements)
    print(f"Среднее арифметическое элементов: {avg:.2f}")
else:
    print("Нет элементов, удовлетворяющих условию.")
