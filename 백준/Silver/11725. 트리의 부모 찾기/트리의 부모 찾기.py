import sys
from collections import deque
import heapq

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
n = int(input())
table = {i: [] for i in range(1, n + 1)}

visited = [False] * (n + 1)

for i in range(n-1):
    nodes = list(map(int, input().split()))
    table[nodes[1]].append(nodes[0])
    table[nodes[0]].append(nodes[1])

res = [0 for _ in range(n+1)]
def dfs(node):
    visited[node] = True
    for neighbors in table[node]:
        if not visited[neighbors]:
            res[neighbors] = node
            dfs(neighbors)

dfs(1)
for i in range(2, n+1):
    print(res[i])
