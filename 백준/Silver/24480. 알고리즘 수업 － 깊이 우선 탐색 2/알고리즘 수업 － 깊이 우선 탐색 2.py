import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m, start = map(int, input().split())
table = {i+1:[] for i in range(n)}
visited = [False] * n

for i in range(m):
    x, y = map(int, input().split())
    table[x].append(y)
    table[y].append(x)

for i in range(n):
    table[i+1].sort(reverse=True)

sequence = {i+1:0 for i in range(n)}
cnt = 0
def dfs(node):
    global cnt
    cnt += 1
    sequence[node] = cnt
    visited[node - 1] = True
    for i in table[node]:
        if not visited[i - 1]:
            dfs(i)

dfs(start)
for i in range(n):
    print(sequence[i+1])