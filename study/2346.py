from collections import deque

n = int(input())
seq_queue = deque(list(map(int, input().split())))
queue = deque([i+1 for i in range(n)])

while seq_queue:
    if len(seq_queue) == 1:
        seq_queue.popleft()
        print(queue.popleft())
        break
    m = seq_queue.popleft()
    if m > 0:
        print(queue.popleft(), end=' ')
        queue.rotate(-(m-1))
        seq_queue.rotate(-(m-1))
    else:
        print(queue.popleft(), end=' ')
        queue.rotate(-m)
        seq_queue.rotate(-m)
#deque에서 rotate는 양수일 때 가장 왼쪽 값이 오른쪽으로 가고 음수일 때 그 반대이다.