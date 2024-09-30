# 11 глава - Задача 4
class Transport:
    def __init__(self, brand, number, speed, capacity):
        self.brand = brand
        self.number = number
        self.speed = speed
        self.capacity = capacity

    def info(self):
        print(f"Транспортное средство: {self.brand}, Номер: {self.number}, Скорость: {self.speed}, Грузоподъемность: {self.capacity}")

    def is_valid_capacity(self, required_capacity):
        return self.capacity >= required_capacity

class Car(Transport):
    def info(self):
        print(f"Автомобиль: {self.brand}, Номер: {self.number}, Скорость: {self.speed}, Грузоподъемность: {self.capacity}")

class Motorcycle(Transport):
    def __init__(self, brand, number, speed, capacity, sidecar=False):
        super().__init__(brand, number, speed, 0 if not sidecar else capacity)
        self.sidecar = sidecar

    def info(self):
        print(f"Мотоцикл: {self.brand}, Номер: {self.number}, Скорость: {self.speed}, Грузоподъемность: {self.capacity}, Коляска: {self.sidecar}")

class Truck(Transport):
    def __init__(self, brand, number, speed, capacity, has_trailer=False):
        super().__init__(brand, number, speed, capacity * (2 if has_trailer else 1))
        self.has_trailer = has_trailer

    def info(self):
        print(f"Грузовик: {self.brand}, Номер: {self.number}, Скорость: {self.speed}, Грузоподъемность: {self.capacity}, Прицеп: {self.has_trailer}")

if __name__ == "__main__":
    vehicles = [
        Car("Toyota", "A123BC", 180, 500),
        Motorcycle("Yamaha", "B456CD", 150, 50, sidecar=True),
        Truck("MAN", "C789EF", 120, 2000, has_trailer=True)
    ]
    for vehicle in vehicles:
        vehicle.info()
        print()

    required_capacity = 1000
    print(f"\nПоиск машин с грузоподъемностью не менее {required_capacity} кг:")
    for vehicle in vehicles:
        if vehicle.is_valid_capacity(required_capacity):
            vehicle.info()
