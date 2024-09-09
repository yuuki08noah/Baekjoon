import sys
from collections import deque
import heapq

input = sys.stdin.readline
n, m, r = map(int, input().split())
items = list(map(int, input().split()))
table = {i:[] for i in range(1, n+1)}
for _ in range(r):
    x, y, z = map(int, input().split())
    table[x].append((y, z))
    table[y].append((x, z))
def dijkstra(q):
    queue = q
    while queue:
        cost, node = heapq.heappop(queue)
        if cost > costs[node-1]:
            continue

        if node in table:
            for next_node, weight in table[node]:
                if weight + cost < costs[next_node-1] and weight + cost <= m:
                    costs[next_node-1] = weight + cost
                    heapq.heappush(queue, (costs[next_node-1], next_node))

m_ = 0
for i in range(1, n+1):
    costs = [float('inf')] * n
    costs[i-1] = 0
    dijkstra([(0, i)])
    res = 0
    for i in range(len(costs)):
        if costs[i] == float('inf'):
            continue
        else:
            res += items[i]
    m_ = max(m_, res)
print(m_)