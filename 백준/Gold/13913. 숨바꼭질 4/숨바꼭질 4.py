import sys
from collections import deque
import heapq

input = sys.stdin.readline
n, m = map(int, input().split())

queue = deque([(n, 0)])
parents = [-1] * (100001)

while queue:
    x, depth = queue.popleft()
    for i in (x - 1, x + 1, 2 * x):
        if 0 <= i <= 100000 and parents[i] == -1:
            parents[i] = x
            queue.append((i, depth + 1))
    if x == m:
        print(depth)
        route = [m]
        while parents[x] != -1 and x != n:
            route.append(parents[x])
            x = parents[x]
        print(*route[::-1])
        break
