import queue
import time
import threading
import random

q = queue.Queue()
print(q.queue)

for i in range(7):
    q.put(i)

print(q.queue)

print(q.empty())
print(q.queue)

while not q.empty():
    print(q.get())

print(q.queue)
print(q.empty())

q = queue.LifoQueue()

for i in range(7):
    q.put(i)

while not q.empty():
    print(q.get())

print("\n")
q = queue.PriorityQueue()
q.put(5)
q.put(4)
q.put(1)
q.put(3)
q.put(2)

while not q.empty():
    print(q.get())

print("\n")
q = queue.Queue()
q.put(6)
print(q.get())

print(q.empty())
# print(q.get())

counter = 1
more_to_come = True

class Producer(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        global counter
        global more_to_come

        for i in range(5):
            time.sleep(random.randrange(2, 5))
            item = "New item #" + str(counter)

            self.queue.put(item)
            counter += 1

            print("\nProduced: ", item)

        more_to_come = False

class Consumer(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):

        while(more_to_come):
            item = self.queue.get(Timeout=10)
            time.sleep(random.random())
            print(threading.current_thread().getName(), " popped: ", item)

        print(threading.current_thread().getName(), " existing...")

q = queue.Queue()

Producer_thread = Producer(q)
Consumer_thread = Consumer(q)

Producer_thread.start()
Consumer_thread.start()