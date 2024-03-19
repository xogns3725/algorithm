import sys
up, down, height = map(int, sys.stdin.readline().split())

# 반복문쓰면 시간초과
# 정상에 올라간 후에는 미끄러지지 않는다
height -= down
day = up - down     # 하루에 올라가는 높이
days = height // day
# 나머지가 생긴만큼 하루 더 올라가줘야하므로
if height % day != 0:
    days += 1

sys.stdout.write(str(days))
