import sys
from collections import deque

input = sys.stdin.readline
n, m, r = map(int, input().split())
table = {i:[] for i in range(1, n+1)}
visited = [True for i in range(0, n+1)]
for i in range(m):
    u, v = map(int, input().split())
    table[u].append(v)
    table[v].append(u)

for i in table.values():
    i.sort()

queue = deque([r])
sequence = [0 for _ in range(n)]
cnt = 1

while queue:
    x = queue.popleft()
    if not visited[x]:
        continue
    sequence[x - 1] = cnt
    cnt += 1
    visited[x] = False
    for node in table[x]:
        if visited[node]:
            queue.append(node)
print(*sequence, sep='\n')