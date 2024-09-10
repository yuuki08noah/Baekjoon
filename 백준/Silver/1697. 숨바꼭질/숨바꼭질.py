import sys
from collections import deque
import heapq

input = sys.stdin.readline
n, m = map(int, input().split())

queue = deque([(n, 0)])
visited = [False] * (100001)
while queue:
    x, depth = queue.popleft()
    if x == m:
        print(depth)
        break
    for i in (x-1, x+1, 2*x):
        if 0 <= i <= 100000 and not visited[i]:
            visited[i] = True
            queue.append((i, depth+1))
