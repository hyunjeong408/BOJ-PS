import sys

def checkParen(str):
    stack  = []
    for k in str:
        if k == '(':
            stack.append(k)
        else:
            if len(stack)>0:
                stack.pop()
            else:
                return False
    if len(stack)>0:
        return False
    return True

n = int(input())

for i in range(n):
    inputStr = sys.stdin.readline().rstrip()
    if checkParen(inputStr):
        print("YES")
    else:
        print("NO")