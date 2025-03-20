import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
s, e = map(int, input().split())
graph = {i:[] for i in range(1, n+1)}
visited = [False for _ in range(n+1)]
for k in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque([(s, 0)])
while queue:
    x, depth = queue.popleft()
    if visited[x]: continue
    visited[x] = True
    if x == e:
        print(depth)
        break
    for y in graph[x] + [x-1, x+1]:
        if 1 <= y <= n and not visited[y]:
            queue.append((y, depth + 1))
