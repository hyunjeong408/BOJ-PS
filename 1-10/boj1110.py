def changeNum(num):
    left = num%10
    if num<10 :
        right = num%10
    else:
        right = (int(num/10) + num%10)%10
    return left*10 + right

n = int(input())
org = n
cycle = 0
while(True):
    n = changeNum(n)
    cycle += 1
    if(n == org):
        break
print(cycle)
