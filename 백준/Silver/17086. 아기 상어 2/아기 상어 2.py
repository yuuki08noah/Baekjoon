import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().strip().split())) for _ in range(n)]
c = [[10**9] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            visited = [[False] * m for _ in range(n)]
            queue = deque([(i, j, 0)])
            c[i][j] = 0
            while queue:
                x, y, cost = queue.popleft()
                if visited[x][y]:
                    continue
                visited[x][y] = True
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, 1), (1, 1), (-1, -1), (1, -1)]:
                    if 0 <= x + dx < n and 0 <= y + dy < m:
                        if board[x + dx][y + dy] == 0 and not visited[x + dx][y + dy]:
                            c[x + dx][y + dy] = min(c[x + dx][y + dy], cost + 1)
                            queue.append((x + dx, y + dy, cost + 1))
mcost = 0
for i in range(n):
    mcost = max(mcost, max(c[i]))
print(mcost)