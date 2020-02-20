from typing import List, Set, Iterable

from config import INPUT_TYPE, OUTPUT_TYPE, PRINT_EVERY_N_DAY
from objects.book import Book
from objects.library import Library
from objects.registry import Registry
from policies import highest_scan_capacity


def sort_signup_libraries(libraries: Iterable[Library]) -> List[Library]:
    return sorted(libraries, key=highest_scan_capacity)


def do_solution(input: INPUT_TYPE) -> OUTPUT_TYPE:
    scanning_days, libraries = input
    not_signed_yet = sort_signup_libraries(libraries)
    signed_order = []
    pending_libraries = []
    registry = Registry()

    for day in range(scanning_days):
        if not day % PRINT_EVERY_N_DAY:
            print(f"Day {day}/{scanning_days}! ({100*day/scanning_days:.2f}%)")

        # Signup process
        if not_signed_yet and not_signed_yet[0].sign_up():
            signed_order.append(not_signed_yet.pop(0))
            pending_libraries.append(signed_order[-1])

        # Remove from pending the empty libraries
        pending_libraries = sorted([library for library in pending_libraries if library.is_has_done_scan()],
                                   key=highest_scan_capacity)

        # Scan for the day
        registry.daily_scan(pending_libraries)
    return signed_order, registry


def get_int_list(line: str) -> List[int]:
    return [int(c) for c in line.split(' ')]


def parse_input(input_content: str) -> INPUT_TYPE:
    lines = input_content.split('\n')
    n_books, n_libraries, n_days = get_int_list(lines.pop(0))
    book_scoring = get_int_list(lines.pop(0))

    books = {i: Book(i, score) for i, score in enumerate(book_scoring)}
    libraries = []

    for library_id in range(n_libraries):
        total_books, signup_time, scan_capacity = get_int_list(lines.pop(0))
        libraries.append(Library(library_id,
                                 {books[book_id] for book_id in get_int_list(lines.pop(0))},
                                 signup_time,
                                 scan_capacity))

    return n_days, libraries


def serialize_output(output: OUTPUT_TYPE) -> str:
    signed_up_sorted_libraries, registry = output
    return registry.serialize(signed_up_sorted_libraries)
