# 9 глава - Задача 4
def sum_less_than(A, znach):
    total_sum = sum(x for x in A if x < znach)
    return total_sum

if __name__ == "__main__":
    A = [1, 2, 3, 4, 5, 6]
    znach = 4
    total_sum = sum_less_than(A, znach)
    print(f"Сумма элементов меньше {znach}: {total_sum}")
