import sys
from collections import deque
import math

input = sys.stdin.readline
n, m = map(int, input().split())
board = []
visited = [[False] * m for _ in range(n)]
for i in range(n):
    board.append(list(map(str, input().strip())))


def bfs():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    queue = deque([(0, 0, 1)])
    while queue:
        x, y, depth = queue.popleft()
        if x == n - 1 and y == m - 1:
            return depth
        for l in range(4):
            nx = x + dx[l]
            ny = y + dy[l]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == '1':
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny, depth + 1))

print(bfs())
# print(*visited, sep='\n')
