import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n, m, k = map(int, input().split())
table = {i:[] for i in range(1, n + 1)}
for i in range(m):
    a, b = map(int, input().split())
    table[a].append(b)
    table[b].append(a)

depths = [-1 for _ in range(n)]

def dfs(node, depth):
    if depths[node-1] == -1:
        depths[node-1] = depth
        for i in sorted(table[node], reverse=True):
            dfs(i, depth + 1)

dfs(k, 0)

print(*depths, sep='\n')