# 11 глава - Задача 11
class Toy:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def info(self):
        print(f"Игрушка: {self.name}, Цена: {self.price}")

    def matches(self, color=None):
        return True

class Cube(Toy):
    def __init__(self, name, price, color, material, edge_size):
        super().__init__(name, price)
        self.color = color
        self.material = material
        self.edge_size = edge_size

    def info(self):
        print(f"Кубик: {self.name}, Цена: {self.price}, Цвет: {self.color}, Материал: {self.material}, Размер ребра: {self.edge_size}")

    def matches(self, color=None):
        return self.color == color if color else True

class Ball(Toy):
    def __init__(self, name, price, color, diameter, material):
        super().__init__(name, price)
        self.color = color
        self.diameter = diameter
        self.material = material

    def info(self):
        print(f"Мяч: {self.name}, Цена: {self.price}, Цвет: {self.color}, Диаметр: {self.diameter}, Материал: {self.material}")

    def matches(self, color=None):
        return self.color == color if color else True

class CarToy(Toy):
    def __init__(self, name, price, manufacturer, color):
        super().__init__(name, price)
        self.manufacturer = manufacturer
        self.color = color

    def info(self):
        print(f"Машинка: {self.name}, Цена: {self.price}, Производитель: {self.manufacturer}, Цвет: {self.color}")

    def matches(self, color=None):
        return self.color == color if color else True

if __name__ == "__main__":
    toys = [
        Cube("Кубик", 500, "красный", "пластик", 5),
        Ball("Мяч", 300, "синий", 20, "резина"),
        CarToy("Машинка", 700, "Hot Wheels", "желтый")
    ]

    for toy in toys:
        toy.info()

    query_color = "синий"
    print(f"\nПоиск игрушек цвета {query_color}:")
    for toy in toys:
        if toy.matches(query_color):
            toy.info()
