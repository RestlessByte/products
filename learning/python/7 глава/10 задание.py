# 7 глава - Задача 10
# Программа для определения длины самого короткого и самого длинного слова
input_string = input("Введите строку: ")
words = input_string.split()
if words:
    min_length = len(min(words, key=len))
    max_length = len(max(words, key=len))
    print(f"Длина самого короткого слова: {min_length}, длина самого длинного слова: {max_length}")
else:
    print("Строка пуста")
