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

def dfs(node, isRoot):
    global cnt
    cnt += 1
    sequence[node] = cnt
    small = sequence[node]

    child = 0
    for vertex in graph[node]:
        if sequence[vertex] == 0:
            child += 1
            low = dfs(vertex, False)
            if not isRoot and low >= sequence[node]:
                res.add(node)
            small = min(small, low)
        else:
            small = min(small, sequence[vertex])
    if isRoot and child >= 2: res.add(node)
    return small

for i in range(1, n+1):
    if sequence[i] == 0:
        dfs(i, True)

print(len(res))
print(*sorted(res))