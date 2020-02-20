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
    scan_relation = min(library.scan_capacity, len(library.books))
    scan_relation_doh = min(library.scan_capacity, len(library.books))
    return scan_relation + highest_book_score(library) / ((library.time or 1) + scan_relation_doh)* -1
