import sys
from collections import deque

input = sys.stdin.readline
graph = [list(map(int, input().split())) for _ in range(5)]
visited = [[0] * 5 for _ in range(5)]
r, c = map(int, input().split())
queue = deque([(r, c, 0)])
while queue:
    x, y, depth = queue.popleft()
    if visited[x][y] != 0: continue
    visited[x][y] = depth
    if graph[x][y] == 1:
        print(depth)
        exit()
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx = x + dx
        ny = y + dy
        if 5 > nx >= 0 and 5 > ny >= 0 == visited[nx][ny] and graph[nx][ny] != -1:
            queue.append((nx, ny, depth + 1))
print(-1)