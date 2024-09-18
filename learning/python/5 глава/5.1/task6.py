# 5 глава - 5.1 Задача 6
# Программа для расчета увеличения вклада в банке с процентной ставкой
deposit = float(input("Введите сумму вклада: "))
rate = float(input("Введите годовой процент: "))
years = int(input("Введите количество лет: "))
for year in range(1, years + 1):
    deposit += deposit * rate / 100
    print(f"Сумма вклада в конце {year} года: {deposit:.2f}")
