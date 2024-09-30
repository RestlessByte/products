# 9 глава - Задача 22
import math

def solve_quadratic(p, q, r):
    D = q**2 - 4*p*r
    if D > 0:
        x1 = (-q + math.sqrt(D)) / (2*p)
        x2 = (-q - math.sqrt(D)) / (2*p)
        return x1, x2
    elif D == 0:
        x = -q / (2*p)
        return x
    else:
        return "Корней нет"

if __name__ == "__main__":
    p = [1, 2, 1]
    q = [2, -3, 0]
    r = [1, 1, -2]
    for i in range(len(p)):
        result = solve_quadratic(p[i], q[i], r[i])
        print(f"Уравнение {i+1}: {result}")
