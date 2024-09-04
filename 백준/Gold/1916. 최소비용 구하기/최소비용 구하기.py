import sys
from collections import deque
import heapq

input = sys.stdin.readline
n = int(input())
m = int(input())
table = {}
costs = [10**9] * n
visited = [False] * n
for _ in range(m):
    x, y, z = map(int, input().split())
    if x not in table:
        table.update({x: [[y, z]]})
    else:
        table[x].append([y, z])

start, end = map(int, input().split())
costs[start-1] = 0

queue = [(start, 0)]
def dijkstra():
    while queue:
        node, cost = heapq.heappop(queue)

        if cost > costs[node-1]:
            continue

        if node in table:
            for next_node, weight in table[node]:
                if weight + cost < costs[next_node-1]:
                    costs[next_node-1] = weight + cost
                    heapq.heappush(queue, (next_node, costs[next_node-1]))
dijkstra()
print(costs[end-1])
