from book_module import Book, EBook
from library import Library
from datetime import date, timedelta


def main():
    book1 = Book("Евгений Онегин", "Пушкин", 1833)
    book2 = Book("Война и мир", "Толстой", 1865)

    ebook1 = EBook(
        "Евгений Онегин", "Пушкин", 1833,
        email="user@example.com"
    )
    ebook1.set_link("email")

    lib = Library()
    lib.add_book(book1)
    lib.add_book(book2)

    lib.show_all()

    print("\n--- Геттеры ---")
    print(f"Название: {book1.get_title()}")
    print(f"Автор: {book1.get_author()}")
    print(f"Год: {book1.get_year()}")

    print("\n--- Сеттеры ---")
    book1.set_author("М. А. Булгаков")
    print(f"Автор обновлён: {book1.get_author()}")
    book1.set_title("")

    print("\n--- Аренда книги ---")
    book2.is_borrowed = True
    book2.borrow_date = date.today() + timedelta(days=book2.borrow_period_days)
    print(book2.get_info())

    print("\n--- Поиск ---")
    found = lib.find_book("Война и нир")
    if found:
        print(f"Найдена: {found.get_info()}")

    print("\n--- Удаление ---")
    lib.remove_book("Евгений онегин")
    lib.show_all()


if __name__ == "__main__":
    main()