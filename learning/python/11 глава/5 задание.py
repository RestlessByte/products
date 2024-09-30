# 11 глава - Задача 5
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def can_afford(self, customer_money):
        return customer_money >= self.price

    def info(self):
        print(f"Товар: {self.name}, Цена: {self.price}")

class Food(Product):
    def __init__(self, name, price, production_date, expiration_date):
        super().__init__(name, price)
        self.production_date = production_date
        self.expiration_date = expiration_date

    def info(self):
        print(f"Продукт: {self.name}, Цена: {self.price}, Дата производства: {self.production_date}, Срок годности: {self.expiration_date}")

class Batch(Product):
    def __init__(self, name, price_per_item, quantity, production_date, expiration_date):
        super().__init__(name, price_per_item * quantity)
        self.price_per_item = price_per_item
        self.quantity = quantity
        self.production_date = production_date
        self.expiration_date = expiration_date

    def info(self):
        print(f"Партия: {self.name}, Цена за штуку: {self.price_per_item}, Количество: {self.quantity}, Общая цена: {self.price}, Дата производства: {self.production_date}, Срок годности: {self.expiration_date}")

class Phone(Product):
    def __init__(self, name, price):
        super().__init__(name, price)

    def info(self):
        print(f"Телефон: {self.name}, Цена: {self.price}")

if __name__ == "__main__":
    products = [
        Food("Яблоко", 50, "2023-09-01", "2023-09-10"),
        Batch("Шоколад", 100, 5, "2023-09-01", "2024-01-01"),
        Phone("iPhone", 70000)
    ]

    for product in products:
        product.info()

    customer_money = 1000
    print(f"\nПокупатель имеет {customer_money} руб. и может купить:")
    for product in products:
        if product.can_afford(customer_money):
            product.info()
