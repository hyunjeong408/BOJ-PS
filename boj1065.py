def hanNum(n):
    g = n%10 - (int(n/10)%10)
    n = int(n/10)
    while(n>=10):
        t = n%10 - (int(n/10)%10)
        if(g != t):
             return False
        n = int(n/10)
    return True

n = int(input())
count = 0
for i in range(1, n+1):
    if(hanNum(i)):
        count += 1
print(count)