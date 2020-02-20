from collections import defaultdict
from typing import Set, List, Dict

from objects.book import Book
from objects.library import Library


class Registry:

    def __init__(self):
        self.internal_registry: Dict[Library, List[Book]] = defaultdict(list)
        pass

    def get_registered_books(self) -> Set[Book]:
        return set(self.internal_registry.values())

    def daily_scan(self, libraries: List[Library]):
        for library in libraries:
            self.internal_registry += list(library.scan(self))
