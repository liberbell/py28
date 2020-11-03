import time
import multiprocessing

def deposit_with_mp(balance, amount):
    for i in range(100):
        time.sleep(0.01)
        balance += amount

    return balance

def withdraw_without_mp(balance, amount):
    for i in range(100):
        time.sleep(0.01)