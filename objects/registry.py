from collections import defaultdict
from typing import Set, List, Dict

from objects.book import Book
from objects.library import Library


class Registry:

    def __init__(self):
        self.internal_registry: Dict[Library, List[Book]] = defaultdict(list)
        self.total_books: Set[Book] = set()
        pass

    def get_registered_books(self) -> Set[Book]:
        return self.total_books

    def daily_scan(self, libraries: List[Library]):
        for library in libraries:
            scanned_books = library.scan(self)
            self.total_books.update(scanned_books)
            self.internal_registry[library] += list(scanned_books)

    def serialize(self, sign_up_sorted_libraries: List[Library]) -> str:
        output = str(len(sign_up_sorted_libraries))

        for library in sign_up_sorted_libraries:
            scanned_books = self.internal_registry[library]
            output += f"\n{str(library.id)} {len(scanned_books)}\n{' '.join([str(book.id) for book in scanned_books])}"

        return output
