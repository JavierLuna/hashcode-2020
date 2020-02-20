import os
import multiprocessing
from typing import List, Tuple

from objects.library import Library
from objects.registry import Registry

base_dir = os.path.dirname(os.path.realpath(__file__))
SOLUTIONS = os.path.join(base_dir, 'solutions')
INPUT = os.path.join(base_dir, 'input')

N_THREADS = None
INPUT_TYPE = Tuple[int, List[Library]]  # Days, libraries
OUTPUT_TYPE = Tuple[List[Library], Registry]  # Libraries by signup, Registry
REGISTRY_TYPE = Registry

INPUT_FILES = [
    "a_example.txt",
    "b_read_on.txt",
    "c_incunabula.txt",
    "d_tough_choices.txt",
    "e_so_many_books.txt",
    "f_libraries_of_the_world.txt"
]

N_THREADS = N_THREADS if N_THREADS is not None else multiprocessing.cpu_count() - 1
