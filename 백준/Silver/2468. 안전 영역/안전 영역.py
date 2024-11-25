import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
d = 0
dy = [0, 0, -1, 1]
dx = [-1, 1, 0, 0]

for i in range(101):
    visited = [[False] * (n + 1) for _ in range(n + 1)]
    cnt = 0
    for j in range(n):
        for k in range(n):
            if board[j][k] - i > 0 and not visited[j][k]:
                cnt += 1
                queue = deque([(j, k)])
                while queue:
                    x, y = queue.popleft()
                    if visited[x][y]:
                        continue
                    visited[x][y] = True
                    for l in range(4):
                        nx = x + dx[l]
                        ny = y + dy[l]
                        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] - i > 0 and not visited[nx][ny]:
                            queue.append((nx, ny))
    d = max(d, cnt)
print(d)