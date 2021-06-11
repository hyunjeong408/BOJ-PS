n =  int(input())
cnt = 0
x = 666
while cnt!=n:
    if str(x).find('666') >= 0:
        cnt += 1
        ans = x
    x += 1
print(ans)