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
    if cmd == "push":
        stack.append(num)
    elif cmd == "pop":
        if len(stack)<1:
            print(-1)
        else:
            print(stack.popleft())
    elif cmd == "size":
        print(len(stack))
    elif cmd == "empty":
        if len(stack)>0:
            print(0)
        else:
            print(1)
    elif cmd == "front":
        if len(stack)>0:
            print(stack[0])
        else:
            print(-1)
    elif cmd == "back":
        if len(stack)>0:
            print(stack[-1])
        else:
            print(-1)