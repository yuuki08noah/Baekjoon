import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
graph = {i:[] for i in range(1, n + 1)}
sequence = []
arr = []
k = 10**9
while True:
    a, b = map(int, input().split())
    if a == b == -1: break
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    visited = [False] * (n + 1)
    m = 0
    queue = deque([(i, 0)])
    while queue:
        x, depth = queue.popleft()
        if visited[x]: continue
        visited[x] = True
        m = max(m, depth)
        for v in graph[x]:
            if not visited[v]:
                queue.append((v, depth + 1))
    k = min(k, m)
    sequence.append((i, m))
    arr.append(m)
print(k, arr.count(k))
for i in sorted(sequence, key=lambda x: x[0]):
    if i[1] == k:
        print(i[0], end=' ')
