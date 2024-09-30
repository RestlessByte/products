# 11 глава - Задача 8
class Client:
    def __init__(self, name, start_date):
        self.name = name
        self.start_date = start_date

    def info(self):
        print(f"Клиент: {self.name}, Дата начала сотрудничества: {self.start_date}")

    def matches_date(self, query_date):
        return self.start_date == query_date

class Depositor(Client):
    def __init__(self, name, start_date, deposit_amount, interest_rate):
        super().__init__(name, start_date)
        self.deposit_amount = deposit_amount
        self.interest_rate = interest_rate

    def info(self):
        print(f"Вкладчик: {self.name}, Дата открытия вклада: {self.start_date}, Размер вклада: {self.deposit_amount}, Процент: {self.interest_rate}")

class Creditor(Client):
    def __init__(self, name, start_date, loan_amount, interest_rate, remaining_debt):
        super().__init__(name, start_date)
        self.loan_amount = loan_amount
        self.interest_rate = interest_rate
        self.remaining_debt = remaining_debt

    def info(self):
        print(f"Кредитор: {self.name}, Дата выдачи кредита: {self.start_date}, Размер кредита: {self.loan_amount}, Процент: {self.interest_rate}, Остаток долга: {self.remaining_debt}")

class Organization(Client):
    def __init__(self, name, start_date, account_number, balance):
        super().__init__(name, start_date)
        self.account_number = account_number
        self.balance = balance

    def info(self):
        print(f"Организация: {self.name}, Дата открытия счета: {self.start_date}, Номер счета: {self.account_number}, Баланс: {self.balance}")

if __name__ == "__main__":
    clients = [
        Depositor("Иван Петров", "2023-01-01", 100000, 5.0),
        Creditor("Сергей Иванов", "2022-07-15", 50000, 12.5, 20000),
        Organization("ООО Альфа", "2021-10-05", "123456789", 250000)
    ]

    for client in clients:
        client.info()

    query_date = "2023-01-01"
    print(f"\nПоиск клиентов, начавших сотрудничество {query_date}:")
    for client in clients:
        if client.matches_date(query_date):
            client.info()
