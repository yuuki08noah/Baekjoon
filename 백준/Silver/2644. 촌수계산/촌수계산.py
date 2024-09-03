import sys
import math
from math import gcd
from collections import deque

input = sys.stdin.readline
n = int(input())
x, y = map(int, input().split())
m = int(input())
visited = [False] * (n + 1)
table = {}
for i in range(m):
    a, b = map(int, input().split())
    if a not in table:
        table.update({a: [b]})
    else:
        table[a].append(b)
    if b not in table:
        table.update({b: [a]})
    else:
        table[b].append(a)

def bfs(start):
    queue = deque([(start, 0)])
    visited[start] = True  # start node 방문 표시
    found = False
    while queue:
        node, depth = queue.popleft()
        if node == y:
            found = True
            print(depth)
            break

        if node in table:
            for i in table[node]:
                if not visited[i]:
                    visited[i] = True
                    queue.append((i, depth + 1))
    return found
if not bfs(x):
    print(-1)
