import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    v, e = map(int, input().split())
    graph = {i:[] for i in range(1, v + 1)}
    color = [None] * (v + 1)
    flag = True

    for i in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    for node in graph.keys():
        if not color[node] and flag:
            queue = deque()
            queue.append((node, 'red'))

            while queue and flag:
                x, c = queue.popleft()
                if color[x]:
                    if color[x] != c:
                        flag = False
                        break
                    continue
                color[x] = c
                for vertex in graph[x]:
                    if color[vertex] == c:
                        flag = False
                        break
                    elif not color[vertex]:
                        queue.append((vertex, 'blue' if c == 'red' else 'red'))
    print('YES') if flag else print('NO')