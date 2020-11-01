import multiprocessing

result = []

def square(num_list):
    global result

    for num in num_list:
        result.append(num * num)

        print("Child process result: ", result)

num_list = [1, 2, 3, 4]

p1 = multiprocessing.Process(target=square, args=(num_list, ))

p1.start()
p1.join()

print("Main process result:", result)