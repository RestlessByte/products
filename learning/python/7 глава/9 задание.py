# 7 глава - Задача 9
# Программа для выделения подстроки между первой и второй точками
input_string = input("Введите строку: ")
first_dot = input_string.find(".")
second_dot = input_string.find(".", first_dot + 1)
if first_dot != -1 and second_dot != -1:
    substring = input_string[first_dot + 1:second_dot]
    print(f"Подстрока между первой и второй точками: {substring}")
else:
    print("Недостаточно точек в строке")
