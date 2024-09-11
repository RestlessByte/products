# 5 глава - Задача 7
# Программа для вычисления количества чисел, которые меньше заданного
threshold = int(input("Введите пороговое значение: "))
count = 0

while True:
    number = int(input("Введите число (0 для выхода): "))
    if number == 0:
        break
    if number < threshold:
        count += 1

print(f"Количество чисел, меньше {threshold}: {count}")
