# 9 глава - Задача 1
def filter_list(A, znach):
    B = [x for x in A if x != znach]
    return B

if __name__ == "__main__":
    A = [1, 2, 3, 4, 5, 2, 6]
    znach = 2
    B = filter_list(A, znach)
    print(f"Новый список B: {B}")
