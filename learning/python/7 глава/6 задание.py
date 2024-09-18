# 7 глава - Задача 6
# Программа для определения самого длинного слова в строке и его количества
input_string = input("Введите строку: ")
words = input_string.split()
if words:
    max_length = max(len(word) for word in words)
    count_max_length = sum(1 for word in words if len(word) == max_length)
    print(f"Самое длинное слово имеет длину {max_length} и встречается {count_max_length} раз(а).")
else:
    print("Строка пуста")
