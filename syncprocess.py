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

    return  balance