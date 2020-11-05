import multiprocessing

def is_even(numbers, q):
    for n in numbers:
        if n % 2 == 0:
            q.put(n)

def print_numbers(q):
    while not q.empty():
        print(q.get())

q = multiprocessing.Queue()

p1 = multiprocessing.Process(target=is_even, args=(range(10), q))