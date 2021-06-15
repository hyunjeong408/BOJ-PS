n, m= map(int, input().split())
cards = []
min_cards = []
for i in range(n):
  card_tmp = list(map(int, input().split()))
  min_cards.append(min(card_tmp))
  cards += card_tmp

import time
start_time = time.time()

print(max(min_cards))

end_time = time.time()
print(end_time-start_time)