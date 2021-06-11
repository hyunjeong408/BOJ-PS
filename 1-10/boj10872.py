def factorial(n):
    ans = 1
    while n>0 :
        ans = ans*n
        n -= 1
    return ans

n = int(input())
print(factorial(n))
