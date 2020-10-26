import queue
import time

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