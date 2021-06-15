n, k = map(int, input().split())

import time
start_time = time.time()

cnt = 0
while n!=1:
  if n%k==0:
    n = n//k
  else:
    n -= 1
  cnt += 1

print(cnt)

end_time = time.time()
print(end_time-start_time)