import sys
import math
from math import gcd
from collections import deque

input = sys.stdin.readline
n, m, k, x = map(int, input().split())
visited = [False] * (n + 1)
table = {}
for i in range(m):
    a, b = map(int, input().split())
    if a not in table:
        table.update({a: [b]})
    else:
        table[a].append(b)

def bfs(start, list):
    queue = deque([(start, 0)])
    visited[start] = True  # start node 방문 표시
    found = False
    while queue:
        node, depth = queue.popleft()

        if depth == k:
            list.append(node)
            found = True
            continue  # 깊이가 k와 같아지면 더 깊이 탐색하지 않음

        if node in table:
            for i in table[node]:
                if not visited[i]:
                    visited[i] = True
                    queue.append((i, depth + 1))
    return found
l = []
if not bfs(x, l):
    print(-1)
else:
    print(*sorted(l), sep='\n')
