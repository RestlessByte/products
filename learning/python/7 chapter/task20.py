# 7 глава - Задача 20
# Программа для удаления всех чисел из строки
import re
input_string = input("Введите строку: ")
result = re.sub(r"\d+", "", input_string)
print(f"Строка после удаления всех чисел: {result}")
