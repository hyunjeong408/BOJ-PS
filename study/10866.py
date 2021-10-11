import sys
from collections import deque

n = int(input())
stack = deque();

for i in range(n):
    inputStr = sys.stdin.readline().rstrip()
    cmdList = inputStr.split(' ')
    num = -1
    if len(cmdList) > 1:
        num = cmdList[1]
    cmd = cmdList[0]
    if cmd == "push_front":
        stack.appendleft(num)
    elif cmd == "push_back":
        stack.append(num)
    elif cmd == "pop_front":
        print(-1) if len(stack)<1 else print(stack.popleft())
    elif cmd == "pop_back":
        print(-1) if len(stack)<1 else print(stack.pop())
    elif cmd == "size":
        print(len(stack))
    elif cmd == "empty":
        print(0) if len(stack)>0 else print(1)
    elif cmd == "front":
        print(stack[0]) if len(stack)>0 else print(-1)
    elif cmd == "back":
        print(stack[-1]) if len(stack)>0 else print(-1)