import sys
from collections import deque
import heapq

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
a, b = map(int, input().split())
arr.insert(0, 0)
queue = [(0, a)]
visited = [-1] * (n + 1)
while queue:
    depth, index = heapq.heappop(queue)
    if visited[index] != -1:
        continue
    visited[index] = depth
    for i in range(index, n + 1, arr[index]):
        if i <= n and visited[i] == -1:
            queue.append((depth + 1, i))
    for i in range(index, 0, -arr[index]):
        if i <= n and visited[i] == -1:
            queue.append((depth + 1, i))
print(visited[b])