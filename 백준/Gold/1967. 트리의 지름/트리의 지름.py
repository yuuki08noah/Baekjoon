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
    table[nodes[0]].append((nodes[1], nodes[2]))
    table[nodes[1]].append((nodes[0], nodes[2]))


def dfs(start, s, l):
    visited[start] = True
    if start in table:
        for nodes in table[start]:
            if not visited[nodes[0]]:
                dfs(nodes[0], s + nodes[1], l)
    heapq.heappush(l, (-s, start))


l = []
dfs(1, 0, l)
far = heapq.heappop(l)
l = []

visited = [False] * (n + 1)
dfs(far[1], 0, l)
next = heapq.heappop(l)
print(max(-far[0], -next[0]))