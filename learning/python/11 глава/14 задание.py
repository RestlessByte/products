# 11 глава - Задача 14
class Currency:
    def __init__(self, amount):
        self.amount = amount

    def to_rubles(self):
        pass

    def info(self):
        print(f"Сумма в рублях: {self.to_rubles()}")

class Dollar(Currency):
    def __init__(self, amount, rate_to_ruble):
        super().__init__(amount)
        self.rate_to_ruble = rate_to_ruble

    def to_rubles(self):
        return self.amount * self.rate_to_ruble

class Euro(Currency):
    def __init__(self, amount, rate_to_ruble):
        super().__init__(amount)
        self.rate_to_ruble = rate_to_ruble

    def to_rubles(self):
        return self.amount * self.rate_to_ruble

if __name__ == "__main__":
    currencies = [
        Dollar(100, 75),   # 1 доллар = 75 рублей
        Euro(50, 90)       # 1 евро = 90 рублей
    ]

    for currency in currencies:
        currency.info()
