# 5 глава - 5.2 Задача 1
# Программа для нахождения максимального значения функции на отрезке [a,b] с шагом h
import math

a = float(input("Введите начало отрезка a: "))
b = float(input("Введите конец отрезка b: "))
h = float(input("Введите шаг h: "))
max_value = -math.inf
x = a

while x <= b:
    value = math.cos(x) / math.sin(x)
    if value > max_value:
        max_value = value
    x += h

print(f"Максимальное значение функции Cos(x)/Sin(x) на отрезке [{a}, {b}] с шагом {h}: {max_value:.2f}")
