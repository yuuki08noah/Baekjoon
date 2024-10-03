import sys
from collections import deque
import heapq

input = sys.stdin.readline
n = int(input())
queue = [(0, n)]
parents = {i: -1 for i in range(1, n+1)}
d = 0
while queue:
    depth, node = heapq.heappop(queue)
    if node == 1:
        if parents[1] == -1:
            parents[1] = node
        d = depth
        break
    if node % 2 == 0:
        if parents[node // 2] == -1:
            heapq.heappush(queue, (depth + 1, node // 2))
            parents[node // 2] = node
    if node % 3 == 0:
        if parents[node // 3] == -1:
            heapq.heappush(queue, (depth + 1, node // 3))
            parents[node // 3] = node
    if node > 1:
        if parents[node - 1] == -1:
            heapq.heappush(queue, (depth + 1, node - 1))
            parents[node - 1] = node
print(d)
route = [1]
index = 1
while parents[index] != -1:
    if parents[index] == 1:
        break
    route.append(parents[index])
    index = parents[index]
route.reverse()
print(*route)
