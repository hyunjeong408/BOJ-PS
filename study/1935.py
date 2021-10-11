n = int(input())
f = input()
numArr = []
stack = []
sign = '+-*/'

for i in range(n):
    numArr.append(int(input()))

for s in f:
    if s in sign:
        b = stack.pop()
        a = stack.pop()
        if s=='+':
            stack.append(a+b)
        elif s=='-':
            stack.append(a-b)
        elif s=='*':
            stack.append(a*b)
        else:
            stack.append(a/b)
    else:
        stack.append(numArr[ord(s)-65])

print("{:.2f}".format(stack[0]))