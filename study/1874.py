import sys

n = int(input())
stack = []
cnt = 1
ansStr = ''

for i in range(n):
    num = int(sys.stdin.readline().rstrip())
    while num>=cnt:
        stack.append(cnt)
        ansStr += '+\n'
        cnt += 1
    if num == stack[-1]:
        stack.pop()
        ansStr += '-\n'
    else:
        ansStr = 'NO'
        break

print(ansStr)