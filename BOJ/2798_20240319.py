N, blakcjack = map(int, input().split())
cards = list(map(int, input().split()))
max_card = 0

for i in range(N):
    for j in range(N):
        for k in range(N):
            # i, j, k 모두 다름
            if i!=j and i!=k and j!=k and max_card < cards[i] + cards[j] + cards[k] <= blakcjack:
                max_card = cards[i] + cards[j] + cards[k]
print(max_card)