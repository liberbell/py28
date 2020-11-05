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
p2 = multiprocessing.Process(target=print_numbers, args=(q, ))

p1.start()
p2.start()

p1.join()
p2.join()

def sender(connection, greets):
    for greet in greets:
        connection.send(greet)
    connection.close()

def recipient(connection):
    while True:
        greet = connection.recv()
        if greet == "STOP":
            break
        print(greet)