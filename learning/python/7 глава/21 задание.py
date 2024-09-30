# 7 глава - Задача 21
# Программа для удаления слова с наибольшей длиной из строки
input_string = input("Введите строку: ")
words = input_string.split()
if words:
    longest_word = max(words, key=len)
    result = input_string.replace(longest_word, "", 1)
    print(f"Строка после удаления самого длинного слова: {result.strip()}")
else:
    print("Строка пуста")
