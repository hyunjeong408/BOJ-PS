import sys

n = int(input())

stack = [];

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
            print(stack.pop())
    elif cmd == "size":
        print(len(stack))
    elif cmd == "empty":
        if len(stack)>0:
            print(0)
        else:
            print(1)
    elif cmd == "top":
        if len(stack)>0:
            print(stack[-1])
        else:
            print(-1)