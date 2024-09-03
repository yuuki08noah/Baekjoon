import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**7)
n, m = map(int, input().split())
table = {}
def f(k):
    if k <= m:
        if k not in table:
            table.update({k: [k + 1, k * 2]})
        if (k + 1) not in table:
            f(k + 1)
        if (k * 2) not in table:
            f(k * 2)
def bfs(q):
    queue = q
    visited = [False] * (m + 1)
    while queue:
        x, depth = queue.popleft()
        visited[x] = True
        # print(x)
        if x == m:
            return depth
        if x in table:
            for i in table[x]:
                if i <= m and not visited[i]:
                    queue.append((i, depth + 1))
                    visited[i] = True
    return -1
q = deque()
q.append((n, 0))
f(n)
# print(table)
print(bfs(q))