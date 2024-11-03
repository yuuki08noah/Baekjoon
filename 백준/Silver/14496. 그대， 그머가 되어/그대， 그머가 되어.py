import sys
from collections import deque
import heapq

input = sys.stdin.readline
a, b = map(int, input().split())
n, m = map(int, input().split())
table = {i:[] for i in range(1, n+1)}
visited = [-1] * (n + 1)
for i in range(m):
    x, y = map(int, input().split())
    table[x].append(y)
    table[y].append(x)
queue = deque([a])
visited[a - 1] = 0
while queue:
    node = queue.popleft()
    for vertex in table[node]:
        if visited[vertex - 1] == -1:
            queue.append(vertex)
            visited[vertex - 1] = visited[node - 1] + 1
print(visited[b - 1])