import sys
from collections import deque
import heapq

input = sys.stdin.readline
n, m = map(int, input().split())
board = [list(map(str, input()[:-1])) for _ in range(n)]

queue = deque([])
for i in range(n):
    for j in range(m):
        if board[i][j] == 'I':
            queue.append((i, j))

res = set()
while queue:
    x, y = queue.popleft()
    if board[x][y] == 'X' or board[x][y] == '^':
        continue
    board[x][y] = '^'
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < m:
            if board[nx][ny] == 'O':
                queue.append((nx, ny))
            if board[nx][ny] == 'P':
                queue.append((nx, ny))
                res.add((nx, ny))
print(len(res) if res else 'TT')
