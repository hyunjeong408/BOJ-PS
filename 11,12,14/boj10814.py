n = int(input())
people = []
for i in range(n):
    age, name = input().split()
    people.append((int(age), name))
people.sort(key=lambda x: x[0])
for j in range(n):
    print(people[j][0], people[j][1], sep=' ')
