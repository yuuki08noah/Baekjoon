import sys
from collections import deque
import math

input = sys.stdin.readline
n, m = map(int, input().split())
board = []
visited = [[False] * m for _ in range(n)]
for i in range(n):
    board.append(list(map(int, input().strip().split())))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def bfs(q):
    queue = q
    while queue:
        x, y = queue.popleft()
        for l in range(4):
            nx = x + dx[l]
            ny = y + dy[l]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    board[nx][ny] = board[x][y] + 1
                    queue.append((nx, ny))

q = deque()
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            q.append((i, j))
            visited[i][j] = True
bfs(q)
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            print(-1, end=' ')
        elif board[i][j] == 0:
            print(0, end=' ')
        else:
            print(board[i][j] - 2, end=' ')
    print()
