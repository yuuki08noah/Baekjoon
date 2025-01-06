import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[-1] * n for _ in range(n)]

def dfs(x, y):
    if visited[x][y] != -1:
        return visited[x][y]
    visited[x][y] = 1
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] > board[x][y]:
            visited[x][y] = max(visited[x][y], dfs(nx, ny) + 1)
    return visited[x][y]

res = 0
for i in range(n):
    for j in range(n):
        res = max(res, dfs(i, j))

print(res)