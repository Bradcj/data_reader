from model import Book


class BookRepository:
    books: list[Book]

    def __init__(self, books: list[Book]) -> None:
        self.books = books

    def find_length(self, name: str) -> list[Book]:
        return [book for book in self.books if name in book['name']]
        # result = []
        # for book in self.books:
        #     if author in book['author']:
        #         result.append(book)
        # return result
