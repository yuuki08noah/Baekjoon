import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
visited = [[False] * n for _ in range(m)]
queue = deque([(0, 0)])
while queue:
    x, y = queue.popleft()
    if visited[x][y]: continue
    visited[x][y] = True
    for dx, dy in ((1, 0), (0, 1)):
        nx = x + dx
        ny = y + dy
        if 0 <= nx < m and 0 <= ny < n and arr[nx][ny] == 1 and not visited[nx][ny]:
            queue.append((nx, ny))
if visited[-1][-1]:
    print("Yes")
else:
    print("No")