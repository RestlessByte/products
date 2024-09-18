# 6 глава - Задача 11
# Программа для удаления первых четырех нулевых элементов из списка
list_A = list(map(int, input("Введите элементы списка через пробел: ").split()))
zeros_removed = 0

for i in range(len(list_A)):
    if list_A[i] == 0:
        list_A[i] = None
        zeros_removed += 1
        if zeros_removed == 4:
            break

list_A = [x for x in list_A if x is not None]
print(f"Обновленный список: {list_A}")
