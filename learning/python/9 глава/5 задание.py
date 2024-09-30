# 9 глава - Задача 5
from functools import reduce

def multiply_list(A):
    return reduce(lambda x, y: x * y, A)

if __name__ == "__main__":
    A = [1, 2, 3, 4]
    product = multiply_list(A)
    print(f"Произведение элементов списка A: {product}")
