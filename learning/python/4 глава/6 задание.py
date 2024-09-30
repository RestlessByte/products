# 4 Chapter - 6 Task
distance = float(input("Введите расстояние в километрах: "))
days = int(input("Введите количество дней пребывания: "))
if days > 7:
    discount = 0.3
else:
    discount = 0.0
price = distance * 5 * (1 - discount)
print(f"Стоимость билета: {price} руб.")
