# 4 Chapter - 10 Task
num1, num2 = map(float, input("Введите два числа: ").split())
if num1 < num2:
    num1 = 0
    num2 = 100
else:
    num1 = 100
    num2 = 0
print(f"Числа после замены: {num1}, {num2}")
