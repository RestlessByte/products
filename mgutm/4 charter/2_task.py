# 4 Chapter - 2 Task
numbers = list(map(float, input("Введите числа через пробел: ").split()))
positive_sum = sum(num for num in numbers if num > 0)
print(f"Сумма положительных чисел: {positive_sum}")
