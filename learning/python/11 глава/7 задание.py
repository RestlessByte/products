# 11 глава - Задача 7
class PhoneBook:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def info(self):
        print(f"Запись: {self.name}, Телефон: {self.phone}")

    def matches(self, query):
        return query.lower() in self.name.lower()

class Person(PhoneBook):
    def __init__(self, name, address, phone):
        super().__init__(name, phone)
        self.address = address

    def info(self):
        print(f"Персона: {self.name}, Адрес: {self.address}, Телефон: {self.phone}")

class Organization(PhoneBook):
    def __init__(self, name, address, phone, fax, contact_person):
        super().__init__(name, phone)
        self.address = address
        self.fax = fax
        self.contact_person = contact_person

    def info(self):
        print(f"Организация: {self.name}, Адрес: {self.address}, Телефон: {self.phone}, Факс: {self.fax}, Контактное лицо: {self.contact_person}")

class Friend(Person):
    def __init__(self, name, address, phone, birthdate):
        super().__init__(name, address, phone)
        self.birthdate = birthdate

    def info(self):
        print(f"Друг: {self.name}, Адрес: {self.address}, Телефон: {self.phone}, Дата рождения: {self.birthdate}")

if __name__ == "__main__":
    entries = [
        Person("Иван Иванов", "ул. Ленина, 12", "123456789"),
        Organization("ООО Пример", "ул. Мира, 20", "987654321", "543216789", "Петр Петров"),
        Friend("Алексей Сидоров", "ул. Свободы, 34", "1122334455", "01.01.1990")
    ]

    for entry in entries:
        entry.info()

    query = "Иван"
    print(f"\nПоиск записей по фамилии {query}:")
    for entry in entries:
        if entry.matches(query):
            entry.info()
