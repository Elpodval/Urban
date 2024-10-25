import multiprocessing
import time

def read_info(name):
    """Считывает данные из файла и добавляет их в локальный список."""
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())

if __name__ == '__main__':
    filenames = [f'./file {num}.txt' for num in range(1, 5)]
    # Линейный вызов
    start_time = time.monotonic()
    for filename in filenames:
        read_info(filename)
    linear_time = time.monotonic() - start_time
    print(f"{linear_time} (линейный)")

    # Многопроцессный вызов
    start_time = time.monotonic()
    with multiprocessing.Pool() as pool:
        pool.map(read_info, filenames)
    multi_process_time = time.monotonic() - start_time
    print(f"{multi_process_time} (многопроцессный)")