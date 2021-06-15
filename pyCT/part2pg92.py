n, m, k = map(int, input().split())
num_list = list(map(int, input().split()))

import time
start_time = time.time()

sorted_list = sorted(num_list)
cnt = 0
ans = 0
for i in range(m):
  if cnt >= k:
    ans += sorted_list[-2]
    cnt = 0
  else:
    ans += sorted_list[-1]
    cnt += 1
  
print(ans)

end_time = time.time()
print(end_time-start_time)