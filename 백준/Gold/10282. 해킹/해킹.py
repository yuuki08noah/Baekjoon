import sys
from collections import deque
import heapq

input = sys.stdin.readline
t = int(input())

def dijkstra(start):
    costs[start-1] = 0
    queue = [(0, start)]
    while queue:
        cost, x = heapq.heappop(queue)
        if cost > costs[x-1]:
            continue
        for k, l in table[x]:
            if k + cost < costs[l-1]:
                costs[l-1] = k + cost
                heapq.heappush(queue, (k + cost, l))
for _ in range(t):
    n, d, c = map(int, input().split())
    table = {i: [] for i in range(1, n+1)}
    costs = [10**9] * n
    for i in range(d):
        a, b, s = map(int, input().split())
        table[b].append((s, a))
        # table[a].append((s, b))
    dijkstra(c)
    # print(costs)
    print(len(costs) - costs.count(10**9), end=" ")
    while 10**9 in costs:
        costs.remove(10**9)
    print(max(costs))


