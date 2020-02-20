from collections import defaultdict
from typing import Set, List, Dict

from objects.book import Book
from objects.library import Library


class Registry:

    def __init__(self):
        self.internal_registry: Dict[Library, List[Book]] = defaultdict(list)
        pass

    def get_registered_books(self) -> Set[Book]:
        registered_books = set()

        for books in self.internal_registry.values():
            registered_books.union(books)

        return registered_books

    def daily_scan(self, libraries: List[Library]):
        for library in libraries:
            self.internal_registry += list(library.scan(self))

    def serialize(self, sign_up_sorted_libraries: List[Library]) -> str:
        output = str(len(self.internal_registry.values()))

        for library in sign_up_sorted_libraries:
            scanned_books = self.internal_registry[library]
            output += f"{str(library.id)} {len(scanned_books)}\n{' '.join([str(book.id) for book in scanned_books])}"

        return output
