import sys
from collections import deque

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    table = {i:[] for i in range(0, n+1)}
    costs = [10**12 for _ in range(n+1)]
    costs[0] = 0

    for i in range(m):
        x, y, cost = map(int, input().split())
        table[x].append((y, cost))
        table[y].append((x, cost))
    for i in range(k):
        x, y, cost = map(int, input().split())
        table[x].append((y, -cost))
    for i in range(1, n + 1):
        table[0].append((i, 0))

    for k in range(n - 1):
        for i in range(1, n+1):
            for node, cost in table[i]:
                if cost + costs[i] < costs[node]:
                    costs[node] = cost + costs[i]

    negative = False
    for i in range(1, n+1):
        for node, cost in table[i]:
            if cost + costs[i] < costs[node]:
                negative = True
                break
        if negative: break

    if negative:
        print('YES')
        continue
    print('NO')