from typing import List, Set


class Book:

    def __init__(self, id: int, score: int):
        self.id = id
        self.score = score

    def __eq__(self, other):
        return isinstance(other, Book) and other.id == self.id

    def __hash__(self):
        return hash(self.id)
