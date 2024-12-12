import sys
from collections import deque

input = sys.stdin.readline
n, m, k = map(int, input().split())
board = [[0] * n for _ in range(m)]
res = []
cnt = 0
for i in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for k in range(x1, x2):
        for j in range(y1, y2):
            board[k][j] = 1

# print(*board, sep='\n')
for i in range(m):
    for j in range(n):
        if board[i][j] == 0:
            queue = deque([(i, j)])
            cnt += 1
            width = 0
            while queue:
                x, y = queue.popleft()
                if board[x][y]: continue
                width += 1
                board[x][y] = 1
                for nx, ny in [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]:
                    if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 0:
                        queue.append((nx, ny))
            res.append(width)
print(cnt)
print(*sorted(res))