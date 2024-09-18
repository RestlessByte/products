# 7 глава - Задача 13
# Программа для проверки, является ли строка правильным скобочным выражением (только круглые скобки)
input_string = input("Введите строку: ")
balance = 0
for char in input_string:
    if char == "(":
        balance += 1
    elif char == ")":
        balance -= 1
    if balance < 0:
        break
if balance == 0:
    print("Строка является правильным скобочным выражением")
else:
    print("Строка не является правильным скобочным выражением")
