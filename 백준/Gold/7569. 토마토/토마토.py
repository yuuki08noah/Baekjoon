import sys
import math
from math import gcd
from collections import deque

input = sys.stdin.readline
n, m, k = map(int, input().split())

board = []
for _ in range(k):
    temp = []
    for _ in range(m):
        temp.append(list(map(int, input().split())))
    board.append(temp)
def bfs(que):
    queue = que
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]  # up, down, left, right
    dz = [1, -1]
    while queue:
        x, y, z = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if board[z][nx][ny] == 0:
                    board[z][nx][ny] += board[z][x][y] + 1
                    queue.append((nx, ny, z))
        for i in range(2):
            nz = z + dz[i]
            if 0 <= nz < k:
                if board[nz][x][y] == 0:
                    board[nz][x][y] += board[z][x][y] + 1
                    queue.append((x, y, nz))

que = deque()
for o in range(k):
    for i in range(m):
        for j in range(n):
            if board[o][i][j] == 1:
                que.append((i, j, o))
bfs(que)
for z in board:
    for row in z:
        if 0 in row:
            print(-1)
            exit()
m_ = -10**9
for z in board:
    for row in z:
        m_ = max(m_, max(row))
print(m_-1)