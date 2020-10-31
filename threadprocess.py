import time
import multiprocessing
import threading

# def square(numbers):
#     for n in numbers:
#         print("Square of %d is %d" %(n, n * n))

# def cube(numbers):
#     for n in numbers:
#         print("Cube of %d is %d" %(n, n * n * n))

num_list = [2, 3, 8, 16, 256, 1024, 4096]

# p1 = multiprocessing.Process(target=square, args=(num_list, ))
# p2 = multiprocessing.Process(target=cube, args=(num_list, ))

# p1.start()
# p2.start()

# p1.join()
# p2.join()

# print("\nCompleted")

square_result = []
# def square(numbers):

#     global square_result

#     for n in numbers:
#         print("Square of %d is %d " %(n, n * n))
#         square_result.append(n * n)

# p1 = multiprocessing.Process(target=square, args=(num_list, ))

# p1.start()
# p1.join()

# print("\nResult: ", square_result)
# print("\nCompleted.")

start_time = time.time()
def square1(numbers):

    global square_result

    for n in numbers:
        print("Square of %d is %d " %(n, n * n))
        square_result.append(n * n)
    
    print("\nWithin the process. Result: ", square_result)

p1 = multiprocessing.Process(target=square1, args=(num_list, ))

p1.start()
p1.join()
end_time = time.time()

print("Multiprocess Completed.")
print(end_time - start_time)

start_time = time.time()
def square2(numbers):

    global square_result

    for n in numbers:
        print("square of %d is %d" %(n, n * n))
        square_result.append(n * n)

p1 = threading.Thread(target=square2, args=(num_list, ))

p1.start()
p1.join()
end_time = time.time()

print("\nResult: ", square_result)
print("Thread Completed.")
print(end_time - start_time)