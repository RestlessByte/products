# 3 глава - Задача 5
# Программа для вычисления объема цилиндра и конуса
import math

R = float(input("Введите радиус основания: "))
H = float(input("Введите высоту: "))

V_cylinder = math.pi * R**2 * H  # Объем цилиндра
V_cone = (1/3) * math.pi * R**2 * H  # Объем конуса

print(f"Объем цилиндра: {V_cylinder:.2f}")
print(f"Объем конуса: {V_cone:.2f}")
