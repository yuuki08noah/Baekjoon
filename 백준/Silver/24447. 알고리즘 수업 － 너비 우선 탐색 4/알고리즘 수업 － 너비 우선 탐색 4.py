import sys
from collections import deque

input = sys.stdin.readline
v, e, s = map(int, input().split())
table = {i:[] for i in range(1, v + 1)}
visited = [-1] * (v + 1)
cnt = 1
res = 0

for i in range(e):
    x, y = map(int, input().split())
    table[x].append(y)
    table[y].append(x)

queue = deque([(s, 0)])

while queue:
    x, depth = queue.popleft()
    if visited[x] != -1:
        continue
    # print(depth, cnt)
    visited[x] = depth
    res += cnt * depth
    cnt += 1
    for n in table[x]:
        if visited[n] == -1:
            queue.append((n, depth + 1))
print(res)

