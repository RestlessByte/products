# 9 глава - Задача 2
def fill_list(size, znach):
    A = [znach for _ in range(size)]
    return A

if __name__ == "__main__":
    size = int(input("Сколько элементов списка следует заполнить? "))
    znach = int(input("Введите числовое значение: "))
    A = fill_list(size, znach)
    print(f"Заполненный список A: {A}")
