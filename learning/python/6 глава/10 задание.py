# 6 глава - Задача 10
# Программа для включения числа D в отсортированный список A[10] с сохранением упорядоченности
import bisect

D = int(input("Введите число D: "))
list_A = sorted(map(int, input("Введите 10 чисел через пробел: ").split()))
bisect.insort(list_A, D)

print(f"Обновленный список: {list_A}")
