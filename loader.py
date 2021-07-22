import csv

from model import Book


def load_db(filename: str) -> list[Book]:
    books = []

    with open(filename) as csv_file:
        reader = csv.DictReader(csv_file, delimiter=',')
        for row in reader:
            row['length'] = str(row['length'])
            books.append(row)
    return books
