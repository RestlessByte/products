# Программа для нахождения суммы положительных и всех отрицательных чисел в последовательности
positive_sum = 0
negative_sum = 0
i = 1

while True:
    try:
        number = float(input(f"Введите число {i}: "))
    except ValueError:
        print("Ошибка: введите корректное число.")  # Если ввод некорректен, просим повторить ввод
        continue

    if number == 0:
        break  # Прерываем цикл, если введено 0
    elif number > 0:
        positive_sum += number
    elif number < 0:
        negative_sum += number

    i += 1  # Увеличиваем счетчик

print(f"Сумма положительных чисел: {positive_sum}")
print(f"Сумма отрицательных чисел: {negative_sum}")
