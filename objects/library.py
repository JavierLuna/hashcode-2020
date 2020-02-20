from typing import Set

from config import REGISTRY_TYPE
from objects.book import Book


class Library:

    def __init__(self, id: int, books: Set[Book], time: int, scan_capacity: int):
        self.id = id
        self.books = books
        self.time = time
        self.scan_capacity = scan_capacity

    def sign_up(self) -> bool:
        for _ in range(self.time):
            yield False
        yield True

    def scan(self, registry: REGISTRY_TYPE) -> Set[Book]:
        self.books = self.books.substraction(registry.get_registered_books())
        capacity = min(self.scan_capacity, len(self.books))
        return {self.books.pop() for _ in range(capacity)}

    def __eq__(self, other):
        return isinstance(other, Library) and other.id == self.id

    def __hash__(self):
        return hash(self.id)
