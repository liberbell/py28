import queue

q = queue.Queue()
print(q.queue)

for i in range(7):
    q.put(i)

print(q.queue)