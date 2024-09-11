# 4 Chapter - 9 Task
x = float(input("Введите значение x: "))
if x > 5:
    y = x ** 2
elif 0 <= x <= 5:
    y = x
else:
    y = 1
print(f"Значение функции: {y}")
