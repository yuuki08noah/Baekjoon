import sys
from collections import deque
import heapq

input = sys.stdin.readline
n, m = map(int, input().split())

queue = [(0, n)]
visited = [10**9] * (100001)
while queue:
    depth, x = heapq.heappop(queue)
    if visited[x] < depth:
        continue
    visited[x] = depth
    if x == m:
        print(depth)
        break
    for i in (x-1, x+1):
        if 0 <= i <= 100000 and visited[i] > depth+1:
            heapq.heappush(queue, (depth+1, i))
    if 0 <= 2*x <= 100000 and visited[2*x] > depth + 1:
        heapq.heappush(queue, (depth, 2*x))
