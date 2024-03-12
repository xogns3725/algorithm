from itertools import permutations

N = int(input())
numbers = set(permutations([i for i in range(1,10)], 3))    # 123~987
for _ in range(N):
    num, strike, ball = map(int, input().split())
    num = list(map(int, str(num)))    # number 각 자릿수별 리스트화

    new_num = set()
    for number in numbers:
        s_cnt, b_cnt = 0, 0
        for i in range(3):
            if num[i] in number:
                if num[i] == number[i]:
                    s_cnt += 1
                else:
                    b_cnt += 1

        if strike == s_cnt and ball == b_cnt:
            new_num.add(number)

    numbers = new_num   #numbers 갱신
    if len(numbers) == 0:
        break

print(len(numbers))