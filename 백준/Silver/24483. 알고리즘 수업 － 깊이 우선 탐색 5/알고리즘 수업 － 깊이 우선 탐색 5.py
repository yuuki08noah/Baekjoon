import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n, m, k = map(int, input().split())
graph = {i:[] for i in range(1, n+1)}
visited = [False] * (n + 1)

res = 0
t = 0
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(n, depth):
    if visited[n]:
        return
    global t, res
    t += 1
    res += t * depth
    visited[n] = True
    for node in sorted(graph[n]):
        if not visited[node]:
            dfs(node, depth + 1)

dfs(k, 0)

print(res)