import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())
costs = [1] * n
minimum = {i: 10**9 for i in range(1, n + 1)}
graphs = {i: [] for i in range(1, n + 1)}
in_degree = {i: 0 for i in range(1, n + 1)}
for i in range(k):
    x, y = map(int, input().split())
    in_degree[x] += 1
    graphs[y].append(x)
queue = deque([])
sequence = []
for node in graphs:
    if len(graphs[node]) == 0:
        minimum[node] = costs[node - 1]

for degree in range(1, len(in_degree)+1):
    if in_degree[degree] == 0:
        queue.append(degree)
while queue:
    y = queue.popleft()
    sequence.insert(0, y)
    if y in graphs:
        for i in graphs[y]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                queue.append(i)

for node in sequence:
    if len(graphs[node]) != 0:
        minimum[node] = min(max([minimum[i] + costs[node - 1] for i in graphs[node]]), minimum[node])
print(*minimum.values())

