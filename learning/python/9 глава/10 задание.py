# 9 глава - Задача 10
def insert_in_order(A, znach):
    A.append(znach)
    A.sort()
    return A

if __name__ == "__main__":
    A = [1, 3, 5, 7]
    znach = 4
    A = insert_in_order(A, znach)
    print(f"Список после вставки: {A}")
