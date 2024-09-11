# 5 глава - 5.1 Задача 2
# Программа для нахождения среднего значения температуры из N значений
N = int(input("Введите количество температур: "))
temperatures = [float(input(f"Введите температуру {i + 1}: ")) for i in range(N)]
average_temperature = sum(temperatures) / N
print(f"Средняя температура: {average_temperature:.2f}")
