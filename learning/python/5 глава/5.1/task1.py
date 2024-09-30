# 5 глава - 5.1 Задача 1
# Программа для подсчета количества отрицательных температур из N значений
N = int(input("Введите количество температур: "))
temperatures = [float(input(f"Введите температуру {i + 1}: ")) for i in range(N)]
negative_count = sum(1 for temp in temperatures if temp < 0)
print(f"Количество отрицательных температур: {negative_count}")
