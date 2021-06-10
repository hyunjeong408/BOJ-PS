m = int(input())
n = int(input())
i = m
prime_num = []

def isPrime(n):
    j = 3
    while j*j <= i:
        if i%j == 0:
            return False
        j += 1
    return True

for i in range(m, n+1):
    if i == 1:
        continue
    elif i%2 == 0:
        if i == 2:
            prime_num.append(i)
    else:
        if isPrime(i):
            prime_num.append(i)

if len(prime_num) != 0:
    print(sum(prime_num))
    print(min(prime_num))
else:
    print(-1)