import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
graph = {i:[] for i in range(1, n+1)}
sequence = {i:0 for i in range(1, n+1)}
cnt = 0
res = set()
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(node, parent):
    global cnt
    cnt += 1
    sequence[node] = cnt
    small = sequence[node]

    for vertex in graph[node]:
        if vertex == parent: continue
        if sequence[vertex] == 0:
            low = dfs(vertex, node)
            if low > sequence[node]:
                res.add(tuple(sorted([node, vertex])))
            small = min(small, low)
        else:
            small = min(small, sequence[vertex])
    return small

for i in range(1, n+1):
    if sequence[i] == 0:
        dfs(i, 0)

print(len(res))
for x, y in sorted(res):
    print(x, y)