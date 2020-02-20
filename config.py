import os
import multiprocessing
from typing import Set

from objects.book import Book
from objects.registry import Registry

base_dir = os.path.dirname(os.path.realpath(__file__))
SOLUTIONS = os.path.join(base_dir, 'solutions')
INPUT = os.path.join(base_dir, 'input')

N_THREADS = None
INPUT_TYPE = str
OUTPUT_TYPE = str
REGISTRY_TYPE = Registry

INPUT_FILES = [

]

N_THREADS = N_THREADS if N_THREADS is not None else multiprocessing.cpu_count() - 1
