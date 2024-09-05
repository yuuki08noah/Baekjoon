import sys
from collections import deque
import heapq
from math import gcd
input = sys.stdin.readline
n, m = map(int, input().split())
table = {i+1: [] for i in range(n)}
visited = [False] * (n + 1)
for _ in range(m):
    x, y = map(int, input().split())
    table[x].append(y)
    table[y].append(x)

cnt = 0
for i in range(1, n + 1):
    if not visited[i]:
        cnt += 1
        visited[i] = True
        q = deque([i])
        while q:
            curr = q.popleft()
            for next_node in table[curr]:
                if not visited[next_node]:
                    visited[next_node] = True
                    q.append(next_node)
print(cnt)