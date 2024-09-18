# Программа для расчета срока, за который вклад превысит 1 миллион рублей и вывода суммы вклада каждый год

initial_deposit = float(input("Введите начальный вклад: "))
rate = float(input("Введите процентную ставку: "))
years = 0
current_deposit = initial_deposit

print(f"Год {years}: {current_deposit:.2f} рублей")  # Вывод начального вклада

while current_deposit <= 1_000_000:
    current_deposit += current_deposit * rate / 100
    years += 1
    print(f"Год {years}: {current_deposit:.2f} рублей")  # Вывод суммы вклада каждый год

print(f"\nВклад превысит 1 миллион рублей через {years} лет.")
print(f"Величина вклада через {years} лет будет: {current_deposit:.2f} рублей.")
