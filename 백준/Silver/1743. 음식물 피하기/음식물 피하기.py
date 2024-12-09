import sys
from collections import deque

input = sys.stdin.readline

n, m, k  = map(int, input().split())
board = [[0] * (m + 1) for _ in range(n + 1)]
maxCnt = 0

for i in range(k):
    a, b = map(int, input().split())
    board[a][b] = 1

for i in range(1, n+1):
    for j in range(1, m+1):
        if board[i][j] == 1:
            queue = deque([(i, j)])
            cnt = 0
            while queue:
                x, y = queue.popleft()
                if board[x][y] == 0:
                    continue
                board[x][y] = 0
                cnt += 1
                for o in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx, ny = x + o[0], y + o[1]
                    if 0 < nx <= n and 0 < ny <= m and board[nx][ny] == 1:
                        queue.append((nx, ny))
            maxCnt = max(maxCnt, cnt)
print(maxCnt)