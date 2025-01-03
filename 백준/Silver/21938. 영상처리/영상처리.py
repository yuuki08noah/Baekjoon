import bisect
import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
for i in range(n):
    l = list(map(int, input().split()))
    temp = []
    while len(l) > 0:
        temp.append(sum(l[:3])/3)
        l = l[3:]
    graph.append(temp)

t = int(input())
graph = list(map(lambda x: list(map(lambda y: int(y >= t), x)), graph))
cnt = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue = deque([(i, j)])
            while queue:
                x, y = queue.popleft()
                if graph[x][y] == 0: continue
                graph[x][y] = 0
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                        queue.append((nx, ny))
            cnt += 1
print(cnt)