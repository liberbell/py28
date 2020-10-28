import time
import multiprocessing

def square(numbers):
    for n in numbers:
        print("Square of %d is %d" %(n, n * n))

def cube(numbers):
    for n in numbers:
        print("Cube of %d is %d" %(n, n * n * n))