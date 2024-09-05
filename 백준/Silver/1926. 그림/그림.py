import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
visited = [[False] * m for _ in range(n)]

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


def dfs(x, y):
    size = 1
    board[x][y] = 2
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] is False:
            if board[nx][ny] == 1:
                size += dfs(nx, ny)
    return size


cnt = 0
p = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            visited[i][j] = True
            cnt += 1
            p.append(dfs(i, j))

print(cnt)
if len(p) != 0:
    print(max(p))
else:
    print(0)