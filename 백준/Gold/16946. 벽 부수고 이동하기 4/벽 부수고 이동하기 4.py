import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(n)]
result = [[0] * m for _ in range(n)]
count = {}
ones = []
k = 2
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(start, index):
    queue = deque([start])
    cnt = 0
    while queue:
        x, y = queue.popleft()
        if board[x][y] != 0:
            continue
        board[x][y] = index
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
                queue.append((nx, ny))
    count[index] = cnt

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            bfs((i, j), k)
            k += 1
        elif board[i][j] == 1:
            ones.append((i, j))

for points in ones:
    i, j = points
    p = set()
    for k in range(4):
        h, o = i + dx[k], j + dy[k]
        if 0 <= h < n and 0 <= o < m:
            if board[h][o] > 1:
                p.add(board[h][o])
    result[i][j] = (sum(count[group] for group in p) + 1) % 10

for i in result:
    print(*i, sep='')