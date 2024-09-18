# 7 глава - Задача 14
# Программа для определения количества слов, содержащих ровно три буквы "е"
input_string = input("Введите строку: ")
words = input_string.split()
count = sum(1 for word in words if word.lower().count("е") == 3)
print(f"Количество слов, содержащих ровно три буквы е: {count}")
