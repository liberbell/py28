import time
import multiprocessing

def deposit_without_mp(balance, amount):
    for i in range(100):
        time.sleep(0.01)
        balance += amount

    return balance

def withdraw_without_mp(balance, amount):
    for i in range(100):
        time.sleep(0.01)
        balance -= amount

    return balance

balance = 600
print(balance)

balance = deposit_without_mp(balance, 5)
print(balance)

balance = withdraw_without_mp(balance, 5)
print(balance)

def deposit_without_lock(balance, amount):
    for i in range(100):
        time.sleep(0.01)
        balance.value += amount

    return  
    
def withdraw_without_lock(balance, amount):
    for i in range(100):
        time.sleep(0.01)
        balance.value -= amount
    
    return balance

balance = multiprocessing.Value("i", 600)
d = multiprocessing.Process(target=deposit_without_lock, args=(balance, 5))
w = multiprocessing.Process(target=withdraw_without_lock, args=(balance, 5))

d.start()
w.start()

d.join()
w.join()

print("Final balance: ", balance.value)

def deposite_with_lock(balance, amount, lock):
    for i in range(100):
        time.sleep(0.01)

        lock.acquire()
        balance.value += amount
        lock.release()

def withdraw_with_lock(balance, amount, lock):
    for i in range(100):
        time.sleep(0.01)

        lock.acquire()
        balance.value -= amount
        lock.release()