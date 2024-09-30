# 7 глава - Задача 23
# Программа для определения, каких букв больше в строке: гласных или согласных
input_string = input("Введите строку: ")
vowels = "AEIOUaeiou"
consonants_count = sum(1 for char in input_string if char.isalpha() and char not in vowels)
vowels_count = sum(1 for char in input_string if char in vowels)
if vowels_count > consonants_count:
    print("Гласных больше")
else:
    print("Согласных больше")
