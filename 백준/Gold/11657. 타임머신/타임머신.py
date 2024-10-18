import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
table = {i:[] for i in range(1, n+1)}
costs = [10**12 for _ in range(n+1)]
costs[1] = 0
for i in range(m):
    x, y, cost = map(int, input().split())
    table[x].append((y, cost))
for k in range(n - 1):
    for i in range(1, n+1):
        for node, cost in table[i]:
            if cost + costs[i] < costs[node]:
                costs[node] = cost + costs[i]
first = costs.copy()
for i in range(1, n+1):
    for node, cost in table[i]:
        if cost + costs[i] < costs[node]:
            costs[node] = cost + costs[i]
second = costs.copy()
if first != second and len(table[1]) != 0:
    print('-1')
    exit()
for cost in costs[2:]:
    if cost >= 10**11:
        print(-1)
    else:
        print(cost)
