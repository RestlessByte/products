# 11 глава - Задача 1
import math

class Figure:
    def area(self):
        pass

    def perimeter(self):
        pass

    def info(self):
        print("Это фигура.")

class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def info(self):
        print(f"Прямоугольник: ширина = {self.width}, высота = {self.height}, площадь = {self.area()}, периметр = {self.perimeter()}")

class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def info(self):
        print(f"Круг: радиус = {self.radius}, площадь = {self.area():.2f}, периметр = {self.perimeter():.2f}")

class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = self.perimeter() / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c

    def info(self):
        print(f"Треугольник: стороны = {self.a}, {self.b}, {self.c}, площадь = {self.area():.2f}, периметр = {self.perimeter()}")

if __name__ == "__main__":
    figures = [Rectangle(4, 5), Circle(3), Triangle(3, 4, 5)]
    for figure in figures:
        figure.info()
