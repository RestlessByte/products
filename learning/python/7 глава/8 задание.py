# 7 глава - Задача 8
# Программа для удаления указанного слова из строки
input_string = input("Введите строку: ")
word_to_remove = input("Введите слово для удаления: ")
result = input_string.replace(word_to_remove, "")
print(f"Строка после удаления слова: {result}")
