import sys
from collections import deque

input = sys.stdin.readline
n, m, k = map(int, input().split()) # n은 노드의 개수, m은 간선의 개수
table = {}
visited_dfs = []
visited_bfs = []

for _ in range(m):
    x, y = map(int, input().split())
    if x not in table:
        table.update({x: [y]})
    else:
        table[x].append(y)
    if y not in table:
        table.update({y: [x]})
    else:
        table[y].append(x)
for i in range(1, n+1):
    if i in table:
        table[i].sort()


def dfs(node):
    visited_dfs.append(node)

    if node in table:
        for neighbor in table[node]:
            if neighbor not in visited_dfs:
                dfs(neighbor)

def bfs(start):
    queue = deque([start])
    visited_bfs.append(start)

    while queue:
        node = queue.popleft()
        if node in table:
            for neighbor in table[node]:
                if neighbor not in visited_bfs:
                    visited_bfs.append(neighbor)
                    queue.append(neighbor)

dfs(k)
bfs(k)

print(*visited_dfs)
print(*visited_bfs)