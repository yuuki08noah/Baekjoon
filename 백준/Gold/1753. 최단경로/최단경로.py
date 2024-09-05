import sys
from collections import deque
import heapq

input = sys.stdin.readline
n, m = map(int, input().split())
start = int(input())
table = {}
costs = [10**9] * n

for _ in range(m):
    x, y, z = map(int, input().split())
    if x not in table:
        table.update({x: [[y, z]]})
    else:
        table[x].append([y, z])

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
for i in costs:
    if i == 10**9:
        print("INF")
    else:
        print(i)