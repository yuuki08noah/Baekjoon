import sys
import math
from math import gcd
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())

board = []
for _ in range(m):
    board.append(list(map(int, input().split())))
def bfs(que):
    queue = que
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]  # up, down, left, right
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if board[nx][ny] == 0:
                    board[nx][ny] += board[x][y] + 1
                    queue.append((nx, ny))

que = deque()
for i in range(m):
    for j in range(n):
        if board[i][j] == 1:
            que.append((i, j))
bfs(que)

for row in board:
    if 0 in row:
        print(-1)
        exit()
m_ = -10**9
for row in board:
    if m_ < max(row):
        m_ = max(row)
print(m_-1)