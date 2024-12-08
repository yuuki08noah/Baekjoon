import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

v, e = map(int, input().split())
graph = {i:[] for i in range(1, v + 1)}
graph_inversed = {i:[] for i in range(1, v + 1)}
visited = [False] * (v + 1)
visited_inversed = [False] * (v + 1)
numbers = [[0, i] for i in range(v + 1)]
num = 1

for i in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph_inversed[b].append(a)

def dfs(n):
    global num
    for node in graph[n]:
        if not visited[node]:
            visited[node] = True
            dfs(node)
    numbers[n][0] = num
    num += 1

def dfs2nd(n, li):
    li.append(n)
    for node in graph_inversed[n]:
        if not visited_inversed[node]:
            visited_inversed[node] = True
            dfs2nd(node, li)

for i in range(1, v + 1):
    if not visited[i]:
        dfs(i)

numbers.sort(key=lambda x:x[0], reverse=True)

re = []
for i in numbers:
    if i[1] == 0:
        continue
    if not visited_inversed[i[1]]:
        visited_inversed[i[1]] = True
        r = []
        dfs2nd(i[1], r)
        re.append(sorted(r) + [-1])
re.sort()
print(len(re))
for i in re:
    print(*i)