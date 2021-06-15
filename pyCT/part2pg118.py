n, m= map(int, input().split())
r, c, d = map(int, input().split())
loads = []
visited = [0]*(n*m)
for i in range(n):
  loads += list(map(int, input().split()))

import time
start_time = time.time()

move = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def curDir(curD):
  if curD == 0:
    return 3
  else:
    return curD-1

def chk4Dir(d, cur):
  for i in range(4):
    d = curDir(d)
    if cur[0]+move[d][0]<n and cur[0]+move[d][0]>=0 and cur[1]+move[d][1]<m and cur[1]+move[d][1]>=0:
      if visited[m*(cur[0]+move[d][0])+(cur[1]+move[d][1])]==0 and loads[m*(cur[0]+move[d][0])+(cur[1]+move[d][1])]==0:
        return d
  return -1

def moveBack(d, cur):
  if d<2:
    tmp = 2
  else:
    tmp = -2
  return tmp

cnt = 1
cur = (r, c)
visited[m*cur[0]+cur[1]] = 1
while True:
  #print(cur, cnt, sep=' ')
  tmpD = chk4Dir(d, cur)
  tmpMove = m*(cur[0]+move[tmpD][0])+(cur[1]+move[tmpD][1])
  if tmpD != -1:
    cur = (cur[0]+move[tmpD][0], cur[1]+move[tmpD][1])
    visited[tmpMove] = 1
    cnt += 1
    d = tmpD
  else:
    chgD = moveBack(d, cur)
    chgMove = m*(cur[0]+move[chgD][0])+(cur[1]+move[chgD][1])
    if loads[chgMove] != 1:
      cur = (cur[0]+move[chgD][0], cur[1]+move[chgD][1])
    else:
      break

print(cnt)

end_time = time.time()
print(end_time-start_time)