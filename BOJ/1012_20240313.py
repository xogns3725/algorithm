from collections import deque
import sys

T = int(sys.stdin.readline())

# bfs 함수 정의
def bfs():
    while queue:
        x, y = queue.popleft()
        # 상, 하, 좌, 우
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # 행렬 범위 제한
            if 0 <= nx < n and 0 <= ny < m and land[nx][ny] == 1:
                queue.append((nx, ny))
                land[nx][ny] = 0  # 방문한 땅은 0

for _ in range(T):
    n, m, k = map(int, sys.stdin.readline().split())
    land = [[0]*m for _ in range(n)]
    count = 0
    for _ in range(k):
        row, col = map(int, sys.stdin.readline().split())
        land[row][col] = 1

    for i in range(n):
        for j in range(m):
            if land[i][j] == 1:
                count += 1
                queue = deque([(i,j)])
                bfs()

    sys.stdout.write(str(count) + '\n')