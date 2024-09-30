# 9 глава - Задача 3
def count_greater_than(A, znach):
    count = sum(1 for x in A if x > znach)
    return count

if __name__ == "__main__":
    A = [1, 2, 3, 4, 5, 6]
    znach = 3
    count = count_greater_than(A, znach)
    print(f"Количество элементов больше {znach}: {count}")
