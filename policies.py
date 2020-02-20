from config import BOOSTING_CAPACITY, BOOSTING_SCORE
from objects.library import Library


def highest_scan_capacity(library: Library) -> int:
    return library.scan_capacity * -1


def lowest_sign_up_time(library: Library) -> int:
    return library.time


def capacity_per_sign_up_time(library: Library) -> int:
    return library.scan_capacity / (library.time or 1) * -1


def highest_book_score(library: Library) -> int:
    return sum(b.score for b in library.books)


def boosted_capacity_per_sign_up_time(library: Library) -> int:
    return library.scan_capacity * BOOSTING_CAPACITY + highest_book_score(library) * BOOSTING_SCORE / (library.time or 1) * -1
