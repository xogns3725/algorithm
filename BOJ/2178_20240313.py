from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())
maze = []

for _ in range(N):
    maze.append(list(map(int, sys.stdin.readline().rstrip())))

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y = queue.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y]+1
                queue.append((nx, ny))
    return maze[N-1][M-1]

sys.stdout.write(str(bfs(0,0)))