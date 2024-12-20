import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = {i:[] for i in range(1, n+1)}
visited = [False] * (n+1)

for i in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

queue = deque([(1, 0)])
visited[1] = True
cnt = 0

while queue:
    x, depth = queue.popleft()
    cnt += 1
    for y in graph[x]:
        if not visited[y] and depth + 1 <= 2:
            queue.append((y, depth + 1))
            visited[y] = True
print(cnt - 1)