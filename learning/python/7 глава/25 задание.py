# 7 глава - Задача 25
# Программа для замены буквы A на букву O в слове
word = input("Введите слово: ")
if "A" in word.upper():
    result = word.replace("A", "O").replace("a", "o")
    print(f"Результат замены: {result}")
else:
    print("Буквы A в слове нет")
