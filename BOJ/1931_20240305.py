n = int(input())
time = []
for i in range(n):
    data = list(map(int,input().split()))
    time.append(data)

time.sort(key=lambda x: (x[1], x[0]))

last = 0
cnt = 0
for start, end in time:
    if start >= last:
        cnt += 1
        last = end
print(cnt)