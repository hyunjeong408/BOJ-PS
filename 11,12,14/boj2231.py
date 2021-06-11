n = int(input())
i = 1
while True:
    tmpArr = []
    for s in str(i):
        tmpArr.append(int(s))
    if sum(tmpArr)+i == n:
        print(i)
        break
    if i>n:
        print(0)
        break
    i += 1
