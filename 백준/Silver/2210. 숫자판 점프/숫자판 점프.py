import sys

input = sys.stdin.readline

board = [input().strip().split() for _ in range(5)]
res = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(n, x, y, cnt):
    if cnt == 6:
        if n not in res: res.append(n)
        return
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(n + board[nx][ny], nx, ny, cnt + 1)

for i in range(5):
    for j in range(5):
        dfs('', i, j, 0)

print(len(res))