# 11 глава - Задача 9
import datetime

class Software:
    def __init__(self, name, developer):
        self.name = name
        self.developer = developer

    def info(self):
        print(f"Программное обеспечение: {self.name}, Разработчик: {self.developer}")

    def is_valid(self):
        pass

class FreeSoftware(Software):
    def info(self):
        print(f"Свободное ПО: {self.name}, Разработчик: {self.developer}")

    def is_valid(self):
        return True

class TrialSoftware(Software):
    def __init__(self, name, developer, install_date, trial_period_days):
        super().__init__(name, developer)
        self.install_date = datetime.datetime.strptime(install_date, "%Y-%m-%d")
        self.trial_period_days = trial_period_days

    def info(self):
        print(f"Условно-бесплатное ПО: {self.name}, Разработчик: {self.developer}, Установлено: {self.install_date.date()}, Срок пробного периода: {self.trial_period_days} дней")

    def is_valid(self):
        current_date = datetime.datetime.now()
        return (current_date - self.install_date).days <= self.trial_period_days

class CommercialSoftware(Software):
    def __init__(self, name, developer, price, install_date, license_period_days):
        super().__init__(name, developer)
        self.price = price
        self.install_date = datetime.datetime.strptime(install_date, "%Y-%m-%d")
        self.license_period_days = license_period_days

    def info(self):
        print(f"Коммерческое ПО: {self.name}, Разработчик: {self.developer}, Цена: {self.price}, Установлено: {self.install_date.date()}, Срок лицензии: {self.license_period_days} дней")

    def is_valid(self):
        current_date = datetime.datetime.now()
        return (current_date - self.install_date).days <= self.license_period_days

if __name__ == "__main__":
    software_list = [
        FreeSoftware("Linux", "Community"),
        TrialSoftware("Photoshop", "Adobe", "2023-09-01", 30),
        CommercialSoftware("Microsoft Office", "Microsoft", 10000, "2023-08-01", 365)
    ]

    for software in software_list:
        software.info()
        print(f"Можно использовать: {Да if software.is_valid() else Нет}\n" )

