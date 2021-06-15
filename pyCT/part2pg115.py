cur = input()

col = int(chr(ord(cur[:1])-48))
row = int(cur[1:])

import time
start_time = time.time()
#print(row, col, sep = ' ')
move = [(-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1)]
cnt = 0
for m in move:
  if row+m[0]>0 and row+m[0]<=8 and col+m[1]>0 and col+m[1]<=8:
    #print(m)
    cnt += 1
print(cnt)

end_time = time.time()
print(end_time-start_time)