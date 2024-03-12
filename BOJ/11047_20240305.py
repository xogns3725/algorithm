cnt, money = list(map(int, input().split()))
coins = []
qt = 0
for i in range(cnt):
    coins.append(int(input()))

for i in reversed(range(cnt)):
    qt += money//coins[i]
    money %= coins[i]

print(qt)