import sys
from collections import deque

input = sys.stdin.readline
f, s, g, u, d = map(int, input().split())
visited = [[False, 10**9]] * (f + 1)

queue = deque([(s, 0)])
while queue:
    x, depth = queue.popleft()
    if visited[x][0]:
        continue
    visited[x] = [True, depth]
    if x == g:
        break

    if 0 < x + u <= f and not visited[x + u][0]:
        queue.append((x + u, depth + 1))
    if 0 < x - d <= f and not visited[x - d][0]:
        queue.append((x - d, depth + 1))

print("use the stairs" if not visited[g][0] else visited[g][1])