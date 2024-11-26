import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
graphs = {i: [] for i in range(1, n + 1)}
in_degree = {i: 0 for i in range(1, n + 1)}
weight = {i: 0 for i in range(1, n + 1)}
costs = {i: 0 for i in range(1, n + 1)}
visited = {i: False for i in range(1, n + 1)}
queue = deque()
for i in range(1, n+1):
    values = list(map(int, input().split()))
    if values[1] == 0:
        queue.append((i, 0))
        costs[i] = values[0]
    for v in values[2:]:
        graphs[v].append(i)
        in_degree[i] += 1
    weight[i] = values[0]

while queue:
    x, depth = queue.popleft()
    if visited[x]:
        continue
    visited[x] = True
    for node in graphs[x]:
        if not visited[node]:
            in_degree[node] -= 1
            costs[node] = max(costs[node], costs[x] + weight[node])
            if in_degree[node] == 0:
                queue.append((node, depth + 1))

print(max(costs.values()))