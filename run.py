import os
from multiprocessing import Queue
from multiprocessing import Process

from config import OUTPUT_TYPE, INPUT_TYPE, SOLUTIONS, INPUT_FILES, INPUT, N_THREADS
from script import serialize_output, parse_input, do_solution


def store_output(file_name: str, output_content: OUTPUT_TYPE):
    with open(os.path.join(SOLUTIONS, file_name), 'w') as output_file:
        print(f"Serializing solution for {file_name}...")
        serialized_output = serialize_output(output_content)
        print(f"Storing solution {file_name}...")
        output_file.write(serialized_output)


def read_input(file_path: str) -> INPUT_TYPE:
    print(f"Reading input '{file_path}'...")
    with open(os.path.join(INPUT, file_path)) as input_file:
        content = input_file.read()
    print(f"Parsing '{file_path}'...")
    content = parse_input(content)
    return content


def monothread_solution(input_file_path: str):
    input_content = read_input(input_file_path)
    print("Executing solution...")
    output = do_solution(input_content)
    store_output(input_file_path, output)
    print(f"\n\n\t\t!!!!!! SOLUTION FOR {input_file_path} is ready !!!!!!\n\n")


def execute_solution(input_queue: Queue):
    while True:
        input_file_path = input_queue.get()
        if input_file_path is None:
            print("Received kill signal, bye!")
            return
        monothread_solution(input_file_path)


if __name__ == '__main__':

    if N_THREADS > 1:
        work_queue = Queue()

        print(f"Spawning {N_THREADS} processes!")
        processes = [Process(target=execute_solution, args=(work_queue,)) for _ in range(N_THREADS)]
        print("Filling work queue...")
        for input_file in INPUT_FILES:
            work_queue.put(input_file)

        print("Adding kill signal...")
        [work_queue.put(None) for _ in processes]
        print("Starting processes...")
        [p.start() for p in processes]
        print("Waiting for the processes to finish...")
        [p.join() for p in processes]
    else:
        print("One process, doing it in main!")
        for input_file in INPUT_FILES:
            monothread_solution(input_file)
