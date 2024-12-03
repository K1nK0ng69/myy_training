import os
from time import perf_counter
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)


if __name__ == '__main__':
    current_dir = r"C:\Users\Ivan\PycharmProjects\Blumbot\.venv"

    filenames = [os.path.join(current_dir, f'file_{number}.txt') for number in range(1, 5)]

    for file in filenames:
        if not os.path.exists(file):
            print(f"Файл не найден: {file}")
            exit(1)

    start_time = perf_counter()
    for filename in filenames:
        read_info(filename)
    linear_time = perf_counter() - start_time
    print(f"Линейный вызов занял: {linear_time:.6f} секунд")

    start_time = perf_counter()
    with Pool() as pool:
        pool.map(read_info, filenames)
    parallel_time = perf_counter() - start_time
    print(f"Многопроцессный вызов занял: {parallel_time:.6f} секунд")
