# 4 Chapter - 5 Task
import math
a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))
d = b ** 2 - 4 * a * c
if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print(f"Корни уравнения: x1 = {x1}, x2 = {x2}")
elif d == 0:
    x = -b / (2 * a)
    print(f"Уравнение имеет один корень: x = {x}")
else:
    print("Уравнение не имеет вещественных корней")
