import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
queue = deque([(0, 0)])
while queue:
    x, y = queue.popleft()
    visited[x][y] = True
    if n > y + board[x][y] >= 0 and not visited[x][y + board[x][y]]:
        queue.append((x, y + board[x][y]))
    if n > x + board[x][y] >= 0 and not visited[x + board[x][y]][y]:
        queue.append((x + board[x][y], y))
print("HaruHaru" if visited[-1][-1] else "Hing")