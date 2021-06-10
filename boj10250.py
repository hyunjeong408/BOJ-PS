n = int(input())
reservations = []
for i in range(n):
    floor, rooms, p = map(int, input().split())
    
    full = int(p/floor)
    remain = p%floor
    if remain == 0:
        remain = floor
        full -= 1
    reservations.append((remain*100)+full+1)

for res in range(n):
    print(reservations[res])