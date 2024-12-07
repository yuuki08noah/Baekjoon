import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
l = 0
r = []
graph = [[] for i in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    graph[y].append(x)

for i in range(1, n + 1):
    queue = deque([i])
    cnt = 1
    visited = [False] * (n + 1)
    visited[i] = True
    while queue:
        x = queue.popleft()
        for node in graph[x]:
            if not visited[node]:
                visited[node] = True
                queue.append(node)
                cnt += 1
    r.append(cnt)
m = max(r)
for i in range(n):
    if r[i] == m:
        print(i + 1, end=' ')
