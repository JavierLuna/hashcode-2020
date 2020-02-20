import os
from typing import Any

base_dir = os.path.dirname(os.path.realpath(__file__))
SOLUTIONS = os.path.join(base_dir, 'solutions')
INPUT = os.path.join(base_dir, 'input')

INPUT_FILES = [

]

INPUT_TYPE = Any
OUTPUT_TYPE = Any


def do_solution(input: INPUT_TYPE):
    pass


def parse_input(input_content: str) -> INPUT_TYPE:
    pass


def parse_output(output: OUTPUT_TYPE) -> str:
    pass


def store_output(file_name: str, output_content: OUTPUT_TYPE):
    with open(os.path.join(OUTPUT_TYPE, file_name), 'w') as output_file:
        output_file.write(parse_output(output_content))


def read_solution(file_path: str) -> INPUT_TYPE:
    with open(os.path.join(SOLUTIONS, file_path)) as input_file:
        content = input_file.read()
    content = parse_input(content)
    return content


for input_file_path in INPUT_FILES:
    input = read_solution(input_file_path)
    output = do_solution(input)
    store_output(input_file_path, output)
