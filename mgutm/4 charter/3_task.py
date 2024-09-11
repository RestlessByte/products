# 4 Chapter - 3 Task
a, b, c = map(float, input("Введите три числа: ").split())
positive_numbers = [n for n in [a, b, c] if n > 0]
if positive_numbers:
    average = sum(positive_numbers) / len(positive_numbers)
    print(f"Положительные числа: {positive_numbers}, Среднее арифметическое: {average}")
else:
    print("Нет положительных чисел")
