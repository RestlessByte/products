# 9 глава - Задача 12
def count_max_elements(A):
    max_value = max(A)
    count = A.count(max_value)
    return max_value, count

if __name__ == "__main__":
    A = [1, 2, 3, 3, 2]
    max_value, count = count_max_elements(A)
    print(f"Максимальное значение: {max_value}, количество таких элементов: {count}")
