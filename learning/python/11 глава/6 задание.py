# 11 глава - Задача 6
class ProductWithAge:
    def __init__(self, name, price, age_limit):
        self.name = name
        self.price = price
        self.age_limit = age_limit

    def is_appropriate_for_age(self, customer_age):
        return customer_age >= self.age_limit

    def info(self):
        print(f"Товар: {self.name}, Цена: {self.price}, Возрастное ограничение: {self.age_limit}")

class Toy(ProductWithAge):
    def __init__(self, name, price, manufacturer, material, age_limit):
        super().__init__(name, price, age_limit)
        self.manufacturer = manufacturer
        self.material = material

    def info(self):
        print(f"Игрушка: {self.name}, Цена: {self.price}, Производитель: {self.manufacturer}, Материал: {self.material}, Возрастное ограничение: {self.age_limit}")

class Book(ProductWithAge):
    def __init__(self, name, author, price, publisher, age_limit):
        super().__init__(name, price, age_limit)
        self.author = author
        self.publisher = publisher

    def info(self):
        print(f"Книга: {self.name}, Автор: {self.author}, Цена: {self.price}, Издательство: {self.publisher}, Возрастное ограничение: {self.age_limit}")

class SportsEquipment(ProductWithAge):
    def __init__(self, name, price, manufacturer, age_limit):
        super().__init__(name, price, age_limit)
        self.manufacturer = manufacturer

    def info(self):
        print(f"Спортинвентарь: {self.name}, Цена: {self.price}, Производитель: {self.manufacturer}, Возрастное ограничение: {self.age_limit}")

if __name__ == "__main__":
    products = [
        Toy("Мяч", 500, "ToyMaker", "Пластик", 3),
        Book("Гарри Поттер", "Дж. К. Роулинг", 1200, "Издательство", 12),
        SportsEquipment("Теннисная ракетка", 3000, "SportsPro", 8)
    ]

    for product in products:
        product.info()

    customer_age = 10
    print(f"\nТовары, подходящие для возраста {customer_age}:")
    for product in products:
        if product.is_appropriate_for_age(customer_age):
            product.info()
