#импортируем библиотеки
import multiprocessing
import random

def square(number):
    return number ** 2

# Создаем список случайных целых чисел (от 1 до 1_000_000)
numbers = [random.randint(-1_000_000, 1_000_000) for _ in range(1_000)]

if __name__ == '__main__':
    process_num = 2
    with multiprocessing.Pool(processes = process_num) as pool:
        squares = pool.map(square, numbers)
    print("\n Список исходных чисел:", numbers)
