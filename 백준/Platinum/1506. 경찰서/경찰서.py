import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
v = int(input())
costs = list(map(int, input().split()))
graph = [[] for _ in range(v+1)]
graph_inversed = [[] for _ in range(v+1)]
for i in range(1, v+1):
    t = list(map(int, input().strip()))
    for j in range(1, v+1):
        if t[j-1]:
            graph[i].append(j)
            graph_inversed[j].append(i)

visited = [False] * (v + 1)
visited_inversed = [False] * (v + 1)
numbers = [[0, i] for i in range(v + 1)]
num = 1

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
        # print(sorted(r, key=lambda x:costs[x-1]))
        re.append(costs[sorted(r, key=lambda x:costs[x-1])[0]-1])

print(sum(re))