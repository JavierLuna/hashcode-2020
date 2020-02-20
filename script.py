from typing import List

from config import INPUT_TYPE, OUTPUT_TYPE
from objects.book import Book
from objects.library import Library


def do_solution(input: INPUT_TYPE) -> OUTPUT_TYPE:
    return ""


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

    return libraries


def serialize_output(output: OUTPUT_TYPE) -> str:
    return output
