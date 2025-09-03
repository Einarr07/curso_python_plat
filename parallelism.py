import multiprocessing as mp

def calculate_square(number):
    square = number * number
    return square

if __name__ == '__main__':
    numbers = [1, 2, 3, 4, 5]

    # Create a pool
    with mp.Pool() as pool:
        result = pool.map(calculate_square, numbers)

    print(f'Result: {result}')