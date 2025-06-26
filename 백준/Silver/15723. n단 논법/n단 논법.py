import sys
from collections import defaultdict

input = sys.stdin.readline
n = int(input())
graph = defaultdict(list)
for _ in range(n):
    statement = input().strip().split(" is ")
    graph[statement[0]].append(statement[1])
m = int(input())

def dfs(base, c, visited):
    if base == c:
        return 1
    if visited[c]:
        return 0
    visited[c] = True
    return sum([dfs(base, i, visited) for i in graph[c]])

for _ in range(m):
    statement = input().strip().split(" is ")
    visited = defaultdict(bool)
    if dfs(statement[1], statement[0], visited) != 0:
        print("T")
    else:
        print("F")
