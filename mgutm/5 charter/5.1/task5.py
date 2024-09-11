# 5 глава - 5.1 Задача 5
# Программа для нахождения минимальной и максимальной температуры из N значений
N = int(input("Введите количество температур: "))
temperatures = [float(input(f"Введите температуру {i + 1}: ")) for i in range(N)]
min_temperature = min(temperatures)
max_temperature = max(temperatures)
print(f"Минимальная температура: {min_temperature:.2f}, Максимальная температура: {max_temperature:.2f}")
