n = int(input())
result = 0
# 생성자 값을 1부터 n까지 1씩 증가
for m in range(n+1):
    # 각 자릿 수 별로 리스트화
    num = list(map(int, str(m)))
    # 분해합 = 각 자릿수의 합 + m(생성자)
    result = sum(num) + m
    if result == n:
        print(m)
        break
    # n까지 반복했는데 생성자가 없는 경우
    elif m == n:
        print(0)