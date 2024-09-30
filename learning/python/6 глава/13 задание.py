# 6 глава - Задача 13
# Программа для отбора шин с диаметрами, отличающимися не более чем на D см и весом не более W кг
import random

diameters = tuple(random.randint(10, 50) for _ in range(10))
weights = tuple(random.randint(20, 100) for _ in range(10))
D = int(input("Введите максимальное различие в диаметре: "))
W = int(input("Введите максимальное различие в весе: "))

print(f"Диаметры шин: {diameters}")
print(f"Веса шин: {weights}")

pairs = [(i, j) for i in range(10) for j in range(i+1, 10)
         if abs(diameters[i] - diameters[j]) <= D and abs(weights[i] - weights[j]) <= W]

if pairs:
    print(f"Подходящие пары шин: {pairs}")
else:
    print("Нет подходящих пар шин")
