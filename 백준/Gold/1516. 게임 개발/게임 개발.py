import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
minimum = {i: 0 for i in range(1, n + 1)}
graphs = {i: [] for i in range(1, n + 1)}
graphs2 = {i: [] for i in range(1, n + 1)}
in_degree = {i: 0 for i in range(1, n + 1)}
out_degree = {i: 0 for i in range(1, n + 1)}
costs = {i: 10**9 for i in range(1, n + 1)}

for i in range(1, n+1):
    values = list(map(int, input().split()))
    for v in values[1:-1]:
        graphs[v].append(i)
        in_degree[i] += 1
        out_degree[v] += 1
    costs[i] = values[0]

queue = deque([])
sequence = []

for degree in range(1, len(in_degree)+1):
    if in_degree[degree] == 0:
        queue.append(degree)
        minimum[degree] = costs[degree]

while queue:
    x = queue.popleft()
    sequence.append(x)
    if x in graphs:
        for i in graphs[x]:
            in_degree[i] -= 1
            if in_degree[i] == 0:
                queue.append(i)

for node in sequence:
    if len(graphs[node]) != 0:
        for i in graphs[node]:
            minimum[i] = max(minimum[i], minimum[node] + costs[i])

print(*minimum.values(), sep='\n')