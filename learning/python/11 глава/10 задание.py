# 11 глава - Задача 10
class Transport:
    def __init__(self, brand, coordinates):
        self.brand = brand
        self.coordinates = coordinates

    def info(self):
        print(f"Транспорт: {self.brand}, Координаты: {self.coordinates}")

    def is_within_coordinates(self, min_coord, max_coord):
        x, y = self.coordinates
        min_x, min_y = min_coord
        max_x, max_y = max_coord
        return min_x <= x <= max_x and min_y <= y <= max_y

class Airplane(Transport):
    def __init__(self, brand, max_speed, max_height, passengers, coordinates):
        super().__init__(brand, coordinates)
        self.max_speed = max_speed
        self.max_height = max_height
        self.passengers = passengers

    def info(self):
        print(f"Самолет: {self.brand}, Макс. скорость: {self.max_speed}, Макс. высота: {self.max_height}, Пассажиры: {self.passengers}, Координаты: {self.coordinates}")

class Car(Transport):
    def __init__(self, brand, number, year, coordinates):
        super().__init__(brand, coordinates)
        self.number = number
        self.year = year

    def info(self):
        print(f"Автомобиль: {self.brand}, Номер: {self.number}, Год выпуска: {self.year}, Координаты: {self.coordinates}")

class Ship(Transport):
    def __init__(self, brand, coordinates, speed, passengers, home_port):
        super().__init__(brand, coordinates)
        self.speed = speed
        self.passengers = passengers
        self.home_port = home_port

    def info(self):
        print(f"Корабль: {self.brand}, Скорость: {self.speed}, Пассажиры: {self.passengers}, Порт приписки: {self.home_port}, Координаты: {self.coordinates}")

if __name__ == "__main__":
    transports = [
        Airplane("Boeing 737", 900, 12000, 180, (50, 30)),
        Car("Toyota", "A123BC", 2019, (40, 20)),
        Ship("Queen Mary", (60, 40), 50, 3000, "Лондон")
    ]

    for transport in transports:
        transport.info()

    print("\nПоиск транспортных средств в пределах координат (30, 10) и (70, 50):")
    for transport in transports:
        if transport.is_within_coordinates((30, 10), (70, 50)):
            transport.info()
