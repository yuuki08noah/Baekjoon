import sys
from collections import deque
import heapq
from math import gcd

input = sys.stdin.readline
n = int(input())
dangerous = []
for _ in range(n):
    dangerous.append(list(map(int, input().split())))

m = int(input())
death = []
for _ in range(m):
    death.append(list(map(int, input().split())))

graph = []
for i in range(0, 501):
    temp = [0] * 501
    for j in range(0, 501):
        for k in range(n):
            d = dangerous[k]
            if (d[0] <= i <= d[2] or d[2] <= i <= d[0]) and (d[1] <= j <= d[3] or d[3] <= j <= d[1]):
                temp[j] = 1
                break
        for k in range(m):
            d = death[k]
            if (d[0] <= i <= d[2] or d[2] <= i <= d[0]) and (d[1] <= j <= d[3] or d[3] <= j <= d[1]):
                temp[j] = 2
                break
    graph.append(temp)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

costs = [[10**9] * 501 for _ in range(501)]
costs[0][0] = 0

def dijkstra():
    queue = [(0, 0, 0)]
    while queue:
        cost, x, y = heapq.heappop(queue)
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < 501 and 0 <= ny < 501 and graph[nx][ny] != 2:
                c = cost + graph[nx][ny]
                if costs[nx][ny] > c:
                    costs[nx][ny] = c
                    heapq.heappush(queue, (c, nx, ny))
dijkstra()
print(costs[500][500] if costs[500][500]!= 10**9 else -1)
