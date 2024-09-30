# 11 глава - Задача 15
class Progression:
    def __init__(self, first_term, difference):
        self.first_term = first_term
        self.difference = difference

    def j_element(self, j):
        pass

    def sum_progression(self, n):
        pass

    def info(self, n):
        print(f"Сумма прогрессии: {self.sum_progression(n)}")

class ArithmeticProgression(Progression):
    def __init__(self, first_term, difference):
        super().__init__(first_term, difference)

    def j_element(self, j):
        return self.first_term + (j - 1) * self.difference

    def sum_progression(self, n):
        return n * (self.first_term + self.j_element(n)) / 2

class GeometricProgression(Progression):
    def __init__(self, first_term, ratio):
        super().__init__(first_term, ratio)

    def j_element(self, j):
        return self.first_term * self.difference ** (j - 1)

    def sum_progression(self, n):
        if self.difference == 1:
            return self.first_term * n
        return self.first_term * (1 - self.difference ** n) / (1 - self.difference)

if __name__ == "__main__":
    progressions = [
        ArithmeticProgression(1, 2),
        GeometricProgression(1, 2)
    ]

    n = 5  # Рассчитать сумму первых 5 членов
    for progression in progressions:
        progression.info(n)
