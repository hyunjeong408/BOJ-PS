def hanoi(n, f, t, r):
# number of disks, from, to, remain(보조막대)
    res = []
    if n==1:
        res.append((f, t))
    else:
        res = res + hanoi(n-1, f, r, t)
        res.append((f, t))
        res = res + hanoi(n-1, r, t, f)
    return res

n = int(input())
ans = hanoi(n, 1, 3, 2)
print(len(ans))
for i in ans:
    print(i[0], i[1], sep=' ')