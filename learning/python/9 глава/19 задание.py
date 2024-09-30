# 9 глава - Задача 19
def replace_elements(A, znach, znach1):
    return [znach1 if x != znach else x for x in A]

if __name__ == "__main__":
    A = [1, 2, 3, 4, 5]
    znach = 2
    znach1 = 0
    A = replace_elements(A, znach, znach1)
    print(f"Измененный список A: {A}")
