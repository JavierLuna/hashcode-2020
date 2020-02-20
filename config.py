import os
import multiprocessing

base_dir = os.path.dirname(os.path.realpath(__file__))
SOLUTIONS = os.path.join(base_dir, 'solutions')
INPUT = os.path.join(base_dir, 'input')

N_THREADS = None
INPUT_TYPE = str
OUTPUT_TYPE = str

INPUT_FILES = [

]

N_THREADS = N_THREADS if N_THREADS is not None else multiprocessing.cpu_count() - 1
