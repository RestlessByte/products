# 9 глава - Задача 7
def delete_by_index(A, K):
    if 0 <= K < len(A):
        A.pop(K)
    return A

if __name__ == "__main__":
    A = [1, 2, 3, 4, 5]
    K = 2
    A = delete_by_index(A, K)
    print(f"Список после удаления элемента с индексом {K}: {A}")
