# 9 глава - Задача 15
import math

def combination(n, m):
    return math.comb(n, m)

if __name__ == "__main__":
    n = 5
    m = 2
    result = combination(n, m)
    print(f"Число сочетаний C({n}, {m}) = {result}")
