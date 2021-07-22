from rich.console import Console
from rich.table import Table

from model import Book


def render_table(books: list[Book]) -> None:
    table = Table(title="Find Length")

    table.add_column('Name', justify='right', style='cyan')
    table.add_column('length', justify='right', style='red')

    for book in books:
        table.add_row(book['name'], book['length'])

    console = Console()
    console.print(table)
