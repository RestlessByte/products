# 7 глава - Задача 16
# Программа для подсчета количества знаков препинания в строке
import string
input_string = input("Введите строку: ")
punctuation_count = sum(1 for char in input_string if char in string.punctuation)
print(f"Количество знаков препинания в строке: {punctuation_count}")
