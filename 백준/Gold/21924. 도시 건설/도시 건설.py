import sys
from collections import deque
import heapq

input = sys.stdin.readline
n, m = map(int, input().split())
sys.setrecursionlimit(4*n)
parents = [-1 for i in range(n)]

def find(x):
    if parents[x] == -1:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    px, py = find(x), find(y)
    if px!= py:
        parents[px] = py

cmd = []
s = 0
for i in range(m):
    temp = list(map(int, input().split()))
    s += temp[2]
    heapq.heappush(cmd, (temp[2], temp[0], temp[1]))

res = 0
for i in range(m):
    cost, a, b = heapq.heappop(cmd)

    if find(a-1) != find(b-1):
        union(a-1, b-1)
        res += cost

print(-1 if parents.count(-1) > 1 else s - res)
