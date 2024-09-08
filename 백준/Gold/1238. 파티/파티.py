import sys
from collections import deque
import heapq

input = sys.stdin.readline
n, m, k = map(int, input().split())
table = {}
visited = [False] * n
for _ in range(m):
    x, y, z = map(int, input().split())
    if x not in table:
        table.update({x: [[y, z]]})
    else:
        table[x].append([y, z])

def dijkstra(q):
    queue = q
    while queue:
        cost, node = heapq.heappop(queue)

        if cost > costs[node-1]:
            continue

        if node in table:
            for next_node, weight in table[node]:
                if weight + cost < costs[next_node-1]:
                    costs[next_node-1] = weight + cost
                    heapq.heappush(queue, (costs[next_node-1], next_node))
res = []
for i in range(1, n+1):
    if i == k:
        res.append(0)
        continue
    temp = 0
    costs = [10**9] * n
    dijkstra([(0, i)])
    temp += costs[k-1]
    costs = [10**9] * n
    dijkstra([(0, k)])
    temp += costs[i-1]
    res.append(temp)
print(max(res))
