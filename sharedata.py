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
print("--------")

def square_list(numlist, result, square_sum):
    for idx, num in enumerate(numlist):
        result[idx] = num * num

    square_sum.value = sum(result)

result = multiprocessing.Array("i", 4)
square_sum = multiprocessing.Value("i")

p = multiprocessing.Process(target=square_list, args=(num_list, result, square_sum))

p.start()
p.join()

print(list(result))