# 3 глава - Задача 3
# Программа для вычисления площади треугольника по формуле Герона
import math

a = float(input("Введите сторону a: "))
b = float(input("Введите сторону b: "))
c = float(input("Введите сторону c: "))

p = (a + b + c) / 2  # Полупериметр
S = math.sqrt(p * (p - a) * (p - b) * (p - c))  # Площадь

print(f"Площадь треугольника: {S:.2f}")
