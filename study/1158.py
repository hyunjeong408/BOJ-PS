from collections import deque

n, k = map(int, input().split())

queue = deque([i+1 for i in range(n)])

arr = []

while len(queue)>0:
    for i in range(k-1):
        queue.append(queue.popleft())
    arr.append(queue.popleft())

print('<'+', '.join(map(str, arr))+'>')