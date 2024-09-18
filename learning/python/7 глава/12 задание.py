# 7 глава - Задача 12
# Программа для определения количества слов, содержащих хотя бы одну букву "е"
input_string = input("Введите строку: ")
words = input_string.split()
count = sum(1 for word in words if "е" in word.lower())
print(f"Количество слов, содержащих хотя бы одну букву е: {count}")
