import sys
from collections import deque
import heapq

input = sys.stdin.readline
n, m = map(int, input().split())

table = {}
costs = [10**9] * n
visited = [False] * n
for _ in range(m):
    x, y, z = map(int, input().split())
    if x not in table:
        table.update({x: [[y, z]]})
    else:
        table[x].append([y, z])
    if y not in table:
        table.update({y: [[x, z]]})
    else:
        table[y].append([x, z])

start, end = map(int, input().split())
costs[0] = 0

def dijkstra(queue):
    while queue:
        cost, node = heapq.heappop(queue)

        if cost > costs[node-1]:
            continue

        if node in table:
            for next_node, weight in table[node]:
                if weight + cost < costs[next_node-1]:
                    costs[next_node-1] = weight + cost
                    heapq.heappush(queue, (costs[next_node-1], next_node))
queue = [(0, 1)]
dijkstra(queue)
res1 = costs[start-1]
res2 = costs[end-1]

costs = [10**9] * n
costs[start-1] = 0
queue = [(0, start)]
dijkstra(queue)
res1 += costs[end-1]

costs = [10**9] * n
costs[end-1] = 0
queue = [(0, end)]
dijkstra(queue)
res2 += costs[start-1]

costs = [10**9] * n
costs[end-1] = 0
queue = [(0, end)]
dijkstra(queue)
res1 += costs[n-1]

costs = [10**9] * n
costs[start-1] = 0
queue = [(0, start)]
dijkstra(queue)
res2 += costs[n-1]
# print(costs)
res = min(res1, res2)
print(res if res < 10**9 else -1)
