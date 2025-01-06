import sys
import heapq

input = sys.stdin.readline
n, m = map(int, input().split())
graph = {i:[] for i in range(1, n + 1)}
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
costs = [10**9] * (n + 1)
s, t = map(int, input().split())
costs[s] = 0

queue = [(0, s)]
while queue:
    cost, node = heapq.heappop(queue)
    if costs[node] < cost:
        continue

    for edge in graph[node]:
        if costs[node] + edge[1] < costs[edge[0]]:
            costs[edge[0]] = costs[node] + edge[1]
            heapq.heappush(queue, (costs[edge[0]], edge[0]))

print(costs[t])