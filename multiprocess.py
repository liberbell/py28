import time

def square(number):

    time.sleep(1)
    result = number * number
    print("The number %d squares to %d " %(number, result))

numbers = [1, 2, 3, 4]
start_time = time.time()

for number in numbers:
    square(number)