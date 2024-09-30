# 11 глава - Задача 3
class Triangle:
    def __init__(self, a, b, angle):
        self.a = a
        self.b = b
        self.angle = angle

    def area(self):
        pass

    def perimeter(self):
        pass

    def info(self):
        print(f"Треугольник: стороны = {self.a}, {self.b}, угол = {self.angle}")

class RightTriangle(Triangle):
    def __init__(self, a, b):
        super().__init__(a, b, 90)

    def area(self):
        return 0.5 * self.a * self.b

    def perimeter(self):
        return self.a + self.b + (self.a**2 + self.b**2)**0.5

class IsoscelesTriangle(Triangle):
    def __init__(self, a, b):
        super().__init__(a, b, 90)

    def area(self):
        return 0.5 * self.a * self.b

    def perimeter(self):
        return self.a + self.b + self.c
