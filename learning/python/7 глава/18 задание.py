# 7 глава - Задача 18
# Программа для вставки слова после каждого пробела в строке
input_string = input("Введите строку: ")
word_to_insert = input("Введите слово для вставки: ")
result = input_string.replace(" ", " " + word_to_insert + " ")
print(f"Строка после вставки слова: {result}")
