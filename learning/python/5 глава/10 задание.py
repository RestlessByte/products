# 5 глава - Задача 10
# Программа для расчета идеального веса для взрослого человека по формуле: Идеальный вес = Рост - 100
height = int(input("Введите рост (в см): "))
ideal_weight = height - 100

while height != 250:
    height += 1

print(f"Идеальный вес: {ideal_weight} кг")
