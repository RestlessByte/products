# 5 глава - 5.1 Задача 4
# Программа для нахождения максимальной температуры из N значений
N = int(input("Введите количество температур: "))
temperatures = [float(input(f"Введите температуру {i + 1}: ")) for i in range(N)]
max_temperature = max(temperatures)
print(f"Максимальная температура: {max_temperature:.2f}")
