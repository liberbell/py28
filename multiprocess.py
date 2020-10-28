import time
import os
from multiprocessing import Process, current_process

# def square(number):

#     time.sleep(1)
#     result = number * number
#     print("The number %d squares to %d " %(number, result))

# numbers = [1, 2, 3, 4]
# start_time = time.time()

# for number in numbers:
#     square(number)

# end_time = time.time()

# print(end_time - start_time)

def square(number):
    time.sleep(1)
    result = number * number
    process_id = os.getpid()
    print("Process ID: ", process_id)

    print("The number %d squares to %d " %(number, result ))

