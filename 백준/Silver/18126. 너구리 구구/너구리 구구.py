import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
graph = {i:[] for i in range(n+1)}
costs = [0 for _ in range(n+1)]
visited = [False for _ in range(n+1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))
queue = deque([(1, 0)])
while queue:
    x, cost = queue.popleft()
    if costs[x] > cost or visited[x]: continue
    visited[x] = True
    costs[x] = cost
    for w, v in graph[x]:
        if cost + w > costs[v] and not visited[v]:
            queue.append((v, cost+w))

print(max(costs))