import sys
from collections import deque
import heapq

input = sys.stdin.readline
m = int(input())
n = m
table = [list(map(int, list(map(str, input().strip())))) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

distance = [[10**9] * m for _ in range(n)]
distance[0][0] = 0

queue = []
heapq.heappush(queue, (1 if table[0][0] == 0 else 0, 0, 0))
while queue:
    dist, x, y = heapq.heappop(queue)

    if distance[x][y] < dist:
        continue

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            cost = dist + (1 if table[nx][ny] == 0 else 0)
            if cost < distance[nx][ny]:
                distance[nx][ny] = cost
                heapq.heappush(queue, (distance[nx][ny], nx, ny))

print(distance[n-1][m-1])