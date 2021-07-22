from datetime import date
from typing import TypedDict


class Book(TypedDict):
    name: str
    author: str
    length: int
    language: str
    Pubilcation_date: date
    isbn13: str
    publisher: str
