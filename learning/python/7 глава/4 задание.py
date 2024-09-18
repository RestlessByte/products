# 7 глава - Задача 4
# Программа для шифрования введенного текста
input_text = input("Введите текст для шифрования: ")
encrypted_text = "".join(chr(ord(c) - 10) for c in input_text)
print(f"Зашифрованный текст: {encrypted_text}")
