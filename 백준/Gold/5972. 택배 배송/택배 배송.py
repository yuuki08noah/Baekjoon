import sys
from collections import deque
import heapq

input = sys.stdin.readline
n, m = map(int, input().split())
table = {i:[] for i in range(1, n+1)}
costs = [10**9] * n
visited = [False] * n
for _ in range(m):
    x, y, z = map(int, input().split())
    table[x].append([y, z])
    table[y].append([x, z])

start, end = 1, n
costs[start-1] = 0

queue = [(0, start)]
def dijkstra():
    while queue:
        cost, node = heapq.heappop(queue)

        if cost > costs[node-1]:
            continue

        if node in table:
            for next_node, weight in table[node]:
                if weight + cost < costs[next_node-1]:
                    costs[next_node-1] = weight + cost
                    heapq.heappush(queue, (costs[next_node-1], next_node))
dijkstra()
print(costs[end-1])
