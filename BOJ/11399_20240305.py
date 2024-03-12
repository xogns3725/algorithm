n = int(input())
people = list(map(int, input().split()))
sorted_people = sorted(people)
result = 0

for i in range(n):
    for j in range(i+1):
        result += sorted_people[j]

print(result)