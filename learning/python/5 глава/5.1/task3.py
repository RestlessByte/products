# 5 глава - 5.1 Задача 3
# Программа для определения средней отрицательных температур из N значений
N = int(input("Введите количество температур: "))
temperatures = [float(input(f"Введите температуру {i + 1}: ")) for i in range(N)]
negative_temperatures = [temp for temp in temperatures if temp < 0]
if negative_temperatures:
    average_negative = sum(negative_temperatures) / len(negative_temperatures)
    print(f"Средняя отрицательная температура: {average_negative:.2f}")
else:
    print("Отрицательных температур нет")
