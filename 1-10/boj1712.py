x = input()

cost_list = x.split(' ')
fixed = int(cost_list[0])
variable = int(cost_list[1])
cost = int(cost_list[2])

if variable >= cost:
    n = -1
else:
    n = int(fixed/(cost - variable))+1

print(n)
