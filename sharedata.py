import multiprocessing

result = []

def square(num_list):
    global result

    for n in num_list:
        result.append(num * num)
        
