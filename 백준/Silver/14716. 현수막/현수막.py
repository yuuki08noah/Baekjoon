import sys

input = sys.stdin.readline

n, m = map(int, input().split())
sys.setrecursionlimit(10**6)
board = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 0, -1, 1, 1, 1, -1, -1]
dy = [-1, 1, 0, 0, 1, -1, 1, -1]
cnt = 0

def dfs(x, y):
    board[x][y] = 0
    for i in range(8):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1:
            dfs(nx, ny)

for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            cnt += 1
            dfs(i, j)
print(cnt)

