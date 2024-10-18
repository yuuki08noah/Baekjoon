import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
board = [list(map(int, input().strip())) for _ in range(n)]
count = {}
k = 1
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(start, index):
    queue = deque([start])
    cnt = 0
    while queue:
        x, y = queue.popleft()
        if board[x][y] != 1:
            continue
        board[x][y] = -index
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 1:
                queue.append((nx, ny))
    count[index] = cnt

for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            bfs((i, j), k)
            k += 1
print(len(count))
print(*sorted(list(count.values())), sep='\n')
