import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
def dfs(n):
    global num
    for node in graph[n]:
        if not visited[node]:
            visited[node] = True
            dfs(node)
    numbers[n][0] = num
    num += 1

def dfs2nd(n, li):
    group[n] = p
    li.append(n)
    for node in graph_inversed[n]:
        if not visited_inversed[node]:
            visited_inversed[node] = True
            dfs2nd(node, li)

t = int(input())

for _ in range(t):
    v, e = map(int, input().split())
    graph = {i:[] for i in range(v)}
    graph_inversed = {i:[] for i in range(v)}
    visited = [False] * v
    visited_inversed = [False] * v
    numbers = [[0, i] for i in range(v)]
    group = [0] * v
    inDegree = [0] * v
    num = 1
    p = 0

    for i in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph_inversed[b].append(a)

    for i in range(v):
        if not visited[i]:
            dfs(i)

    numbers.sort(key = lambda x:x[0], reverse = True)

    re = []
    for i in numbers:
        if not visited_inversed[i[1]]:
            visited_inversed[i[1]] = True
            r = []
            dfs2nd(i[1], r)
            re.append(r)
            p += 1

    for i in range(v):
        for node in graph[i]:
            if group[node] != group[i]:
                inDegree[group[node]] = 1

    l = 0
    k = []
    for i in range(0, len(re)):
        if inDegree[i] == 0:
            l += 1
            k = re[i]

    if l == 1:
        print(*sorted(k), sep='\n')
    else:
        print("Confused")
    print()
    input()