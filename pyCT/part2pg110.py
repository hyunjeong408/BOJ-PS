n = int(input())
move_list = list(input().split())

move = {'L': (-1, 0), 'R': (1, 0), 'U': (0, -1), 'D': (0, 1)}

def canMove(cur, mv, n):
  hor = cur[0]+mv[0]
  ver = cur[1]+mv[1]
  if hor<1 or hor>n:
    return False
  elif ver<1 or ver>n:
    return False
  else:
    return True

import time
start_time = time.time()

cur = (1, 1)
for mv in move_list:
  if canMove(cur, move[mv], n):
    hor = cur[0]+move[mv][0]
    ver = cur[1]+move[mv][1]
    cur = (hor, ver)

print(cur[1], cur[0], sep=' ')

end_time = time.time()
print(end_time-start_time)