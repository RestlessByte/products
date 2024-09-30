# 11 глава - Задача 12
import math

class Body:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def volume(self):
        pass

    def info(self):
        print(f"Тело: {self.name}, Площадь: {self.area():.2f}, Объем: {self.volume():.2f}")

class Parallelepiped(Body):
    def __init__(self, width, height, length):
        super().__init__("Параллелепипед")
        self.width = width
        self.height = height
        self.length = length

    def area(self):
        return 2 * (self.width * self.height + self.height * self.length + self.length * self.width)

    def volume(self):
        return self.width * self.height * self.length

class Sphere(Body):
    def __init__(self, radius):
        super().__init__("Шар")
        self.radius = radius

    def area(self):
        return 4 * math.pi * self.radius**2

    def volume(self):
        return (4/3) * math.pi * self.radius**3

class Pyramid(Body):
    def __init__(self, base_area, height):
        super().__init__("Пирамида")
        self.base_area = base_area
        self.height = height

    def area(self):
        # Упрощенная формула: площадь основания плюс площадь боковой поверхности
        return self.base_area + 0.5 * self.base_area * self.height

    def volume(self):
        return (1/3) * self.base_area * self.height

if __name__ == "__main__":
    bodies = [
        Parallelepiped(2, 3, 4),
        Sphere(5),
        Pyramid(6, 10)
    ]

    for body in bodies:
        body.info()
