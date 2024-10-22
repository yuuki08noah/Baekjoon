import sys
from collections import deque
import heapq

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
queue = [(0, arr[0], 0)]
visited = [-1] * n
while queue:
    depth, node, index = heapq.heappop(queue)
    if visited[index] != -1:
        continue
    visited[index] = depth
    for i in range(index + 1, index + node + 1):
        if i < n and visited[i] == -1:
            queue.append((depth + 1, arr[i], i))
print(visited[-1])
# print(visited)