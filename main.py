from model import Book
from loader import load_db
from repository import BookRepository
from render import render_table


def main():
    books = load_db('./helper_files/book-db.csv')
    repository = BookRepository(books)
    inputs = input("Enter the title -> ")
    result: list[Book] = repository.find_length(inputs)
    render_table(result)


if __name__ == '__main__':
    main()
