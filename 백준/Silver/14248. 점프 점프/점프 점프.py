import sys
from collections import deque
import heapq

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)
s = int(input())
queue = deque([(arr[s], s)])
visited = [False] * (n + 1)
while queue:
    node, index = queue.popleft()
    if visited[index]:
        continue
    visited[index] = True
    if 1 <= index + node <= n and not visited[index + node]:
        queue.append((arr[index + node], index + node))
    if 1 <= index - node <= n and not visited[index - node]:
        queue.append((arr[index - node], index - node))
# print(visited)
print(visited.count(True))