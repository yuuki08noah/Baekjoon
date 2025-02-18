import sys
import heapq

input = sys.stdin.readline
n, m = map(int, input().split())
graph = {i:[i+1, i+2, i+3, i+4, i+5, i+6] for i in range(1, 101)}
visited = [False] * 101
for i in range(n + m):
    x, y = map(int, input().split())
    graph[x] = [y]

queue = [(0, 1)]
while queue:
    depth, x = heapq.heappop(queue)
    if visited[x]: continue
    visited[x] = True
    if x == 100:
        print(depth)
        exit()
    if len(graph[x]) == 1:
        heapq.heappush(queue, (depth, graph[x][0]))
    else:
        for y in graph[x]:
            if y > 100: continue
            if visited[y]: continue
            heapq.heappush(queue, (depth + 1, y))
