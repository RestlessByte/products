# 11 глава - Задача 2
class Publication:
    def info(self):
        pass

    def is_match(self, author_name):
        return False

class Book(Publication):
    def __init__(self, title, author, year, publisher):
        self.title = title
        self.author = author
        self.year = year
        self.publisher = publisher

    def info(self):
        print(f"Книга: {self.title}, Автор: {self.author}, Год: {self.year}, Издательство: {self.publisher}")

    def is_match(self, author_name):
        return self.author == author_name

class Article(Publication):
    def __init__(self, title, author, journal, number, year):
        self.title = title
        self.author = author
        self.journal = journal
        self.number = number
        self.year = year

    def info(self):
        print(f"Статья: {self.title}, Автор: {self.author}, Журнал: {self.journal}, Номер: {self.number}, Год: {self.year}")

    def is_match(self, author_name):
        return self.author == author_name

class EResource(Publication):
    def __init__(self, title, author, link, annotation):
        self.title = title
        self.author = author
        self.link = link
        self.annotation = annotation

    def info(self):
        print(f"Электронный ресурс: {self.title}, Автор: {self.author}, Ссылка: {self.link}, Аннотация: {self.annotation}")

    def is_match(self, author_name):
        return self.author == author_name

if __name__ == "__main__":
    publications = [Book("Книга 1", "Иванов", 2021, "Издательство 1"),
                    Article("Статья 1", "Петров", "Журнал 1", 5, 2020),
                    EResource("Ресурс 1", "Сидоров", "www.example.com", "Описание")]
    for pub in publications:
        pub.info()
    search_author = "Иванов"
    print(f"\nПоиск по автору {search_author}:")
    for pub in publications:
        if pub.is_match(search_author):
            pub.info()
