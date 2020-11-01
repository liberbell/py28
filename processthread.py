import time
import multiprocessing

# def square(numbers):
#     for n in numbers:
#         print("Square of %d is %d" %(n, n * n))

# def cube(numbers):
#     for n in numbers:
#         print("Cube of %d is %d" %(n, n * n * n))

num_list = [2, 3, 8]

# p1 = multiprocessing.Process(target=square, args=(num_list, ))
# p2 = multiprocessing.Process(target=cube, args=(num_list, ))

# p1.start()
# p2.start()

# p1.join()
# p2.join()

# print("\nComplited")

square_result = []

def square(numbers):
    global square_result

    for n in numbers:
        print("Square of %d is %d" %(n, n * n))
        square_result.append(n * n)

p1 = multiprocessing.Process(target=square, args=(num_list, ))

p1.start()
p1.join()

print("\nReuslt: ", square_result)
print("\nComplited")