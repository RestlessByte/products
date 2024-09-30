# 7 глава - Задача 19
# Программа для нахождения суммы чисел, встречающихся в строке
import re
input_string = input("Введите строку: ")
numbers = map(int, re.findall(r"\d+", input_string))
sum_of_numbers = sum(numbers)
print(f"Сумма чисел в строке: {sum_of_numbers}")
