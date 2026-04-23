from datetime import date

class Book:

    def __init__(self, title: str, author: str, year: int):
        self.__title = title
        self.__author = author
        self.__year = year

        self.borrow_date = None
        self.is_borrowed = False
        self.borrow_period_days = 14

    def get_info(self) -> str:
        status = f"взята до {self.borrow_date}" if self.is_borrowed else "свободна"
        return f'"{self.__title}" — {self.__author} ({self.__year}) [{status}]'

    def get_title(self) -> str:
        return self.__title

    def get_author(self) -> str:
        return self.__author

    def get_year(self) -> int:
        return self.__year

    def set_title(self, new_title: str):
        if new_title.strip():
            self.__title = new_title
        else:
            print("Название не может быть пустым!")

    def set_author(self, author: str):
        self.__author = author

    def set_year(self, year: int):
        if 1000 <= year <= date.today().year:
            self.__year = year
        else:
            print(f"Год должен быть от 1000 до {date.today().year}")

class EBook(Book):

    def __init__(self, title: str, author: str,
                 year: int, email: str):
        super().__init__(title, author, year)
        self.email = email
        self.__link = None

    def set_link(self, link: str):
        self.__link = link

    def get_info(self) -> str:
        base = super().get_info()
        link_info = self.__link if self.__link else "нет ссылки"
        return f"{base} | {self.email} | {link_info}"