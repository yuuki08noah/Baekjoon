import sys
from collections import deque
import heapq

input = sys.stdin.readline
n = int(input())
m = int(input())
parents = [-1 for i in range(0, n+1)]
def union(u, v):
    if find(u) < find(v):
        parents[find(u)] = find(v)
    else:
        parents[find(v)] = find(u)

def find(x):
    if parents[x] == -1:
        return x
    parents[x] = find(parents[x])
    return parents[x]

costs = []
for i in range(m):
    t = list(map(int, input().split()))
    heapq.heappush(costs, (t[2], t[0], t[1]))

res = 0
for i in range(m):
    cost, u, v = heapq.heappop(costs)
    if find(u) != find(v):
        union(u, v)
        res += cost
print(res)
