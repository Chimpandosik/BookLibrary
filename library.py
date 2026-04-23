from book_module import Book

class Library:

    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)
        print(f'Добавлена: "{book.get_title()}"')

    def remove_book(self, title: str):
        for book in self.books:
            if book.get_title().lower() == title.lower():
                self.books.remove(book)
                print(f'Удалена: "{title}"')
                return
        print(f'Книга "{title}" не найдена')

    def find_book(self, title: str) -> Book:
        for book in self.books:
            if book.get_title().lower() == title.lower():
                return book
        return None

    def show_all(self):
        if not self.books:
            print("📭 Библиотека пуста")
            return
        print("\n📚 Все книги в библиотеке:")
        for i, book in enumerate(self.books, 1):
            print(f"  {i}. {book.get_info()}")