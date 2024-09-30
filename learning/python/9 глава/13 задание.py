# 9 глава - Задача 13
def insert_by_index(A, znach, K):
    A.insert(K, znach)
    return A

if __name__ == "__main__":
    A = [1, 2, 3, 4]
    znach = 5
    K = 2
    A = insert_by_index(A, znach, K)
    print(f"Список после вставки значения {znach} на индекс {K}: {A}")
