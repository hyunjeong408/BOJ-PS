from collections import deque
cases = int(input())

for c in range(cases):
    cnt = 1
    n, m = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    idxQueue = deque([i for i in range(len(queue))])
    while True:
        if queue[0] == max(queue):
            if idxQueue[0] == m:
                print(cnt)
                break
            else:
                queue.popleft()
                idxQueue.popleft()
                cnt += 1
        else:
            queue.rotate(-1)
            idxQueue.rotate(-1)