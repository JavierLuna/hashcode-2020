from typing import Set

from config import REGISTRY_TYPE
from objects.book import Book


class Library:

    def __init__(self, id: int, books: Set[Book], time: int, max_books_scanned: int, registry: REGISTRY_TYPE):
        self.id = id
        self.books = books
        self.time = time
        self.max_books_scanned = max_books_scanned

    def sign_up(self) -> bool:
        for _ in range(self.time):
            yield False
        yield True

    def scan(self) -> bool:
        return False
