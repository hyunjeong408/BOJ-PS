n, m = map(int, input().split())
cards = list(map(int, input().split()))

sorted_cards = sorted(cards)
sorted_cards.reverse()

sum = 0
flag = False
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            if (sorted_cards[i]+sorted_cards[j]+sorted_cards[k]) <= m:
                if sum < sorted_cards[i]+sorted_cards[j]+sorted_cards[k]:
                    sum = sorted_cards[i]+sorted_cards[j]+sorted_cards[k]

print(sum)
