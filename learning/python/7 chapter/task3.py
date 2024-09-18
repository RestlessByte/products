# 7 глава - Задача 3
# Программа для вычисления средней длины слов в строке
input_string = input("Введите строку: ")
words = input_string.split()
average_length = sum(len(word) for word in words) / len(words) if words else 0
print(f"Средняя длина слов: {average_length:.2f}")
