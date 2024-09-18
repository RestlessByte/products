# 5 глава - 5.2 Задача 3
# Программа для определения, каких чисел больше в последовательности: положительных или отрицательных
N = int(input("Введите количество элементов последовательности: "))
positive_count = 0
negative_count = 0
i = 1

while i <= N:
    number = float(input(f"Введите число {i}: "))
    if number > 0:
        positive_count += 1
    elif number < 0:
        negative_count += 1
    i += 1

if positive_count > negative_count:
    print("Положительных чисел больше")
elif negative_count > positive_count:
    print("Отрицательных чисел больше")
else:
    print("Количество положительных и отрицательных чисел равно")
