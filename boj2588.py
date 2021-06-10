num1 = int(input())
num2 = int(input())

l1 = num2%10 * num1
l2 = (int(num2/10))%10 * num1
l3 = (int(num2/100))%10 * num1

ans = l1 + l2*10 + l3*100

print(l1, l2, l3, ans, sep='\n')