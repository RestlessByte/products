# 11 глава - Задача 13
import math

class Equation:
    def __init__(self, name):
        self.name = name

    def solve(self):
        pass

    def info(self):
        print(f"Уравнение: {self.name}, Решение: {self.solve()}")

class LinearEquation(Equation):
    def __init__(self, a, b):
        super().__init__("Линейное уравнение")
        self.a = a
        self.b = b

    def solve(self):
        if self.a != 0:
            return -self.b / self.a
        else:
            return "Нет решения" if self.b != 0 else "Бесконечное количество решений"

class QuadraticEquation(Equation):
    def __init__(self, a, b, c):
        super().__init__("Квадратное уравнение")
        self.a = a
        self.b = b
        self.c = c

    def solve(self):
        D = self.b**2 - 4 * self.a * self.c
        if D > 0:
            x1 = (-self.b + math.sqrt(D)) / (2 * self.a)
            x2 = (-self.b - math.sqrt(D)) / (2 * self.a)
            return x1, x2
        elif D == 0:
            x = -self.b / (2 * self.a)
            return x
        else:
            return "Нет вещественных корней"

if __name__ == "__main__":
    equations = [
        LinearEquation(2, -4),
        QuadraticEquation(1, -3, 2),
        QuadraticEquation(1, 2, 1)
    ]

    for equation in equations:
        equation.info()
