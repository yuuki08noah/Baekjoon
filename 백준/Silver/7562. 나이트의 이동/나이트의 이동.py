import sys
from collections import deque

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    a, b = map(int, input().split())
    x, y = map(int, input().split())
    visited = [[False] * n for _ in range(n)]
    queue = deque([(a, b, 0)])
    while queue:
        p, q, r = queue.popleft()
        if visited[p][q]: continue
        visited[p][q] = True
        if p == x and q == y:
            print(r)
            break
        for dx, dy in ((-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (1, -2), (2, -1)):
            nx, ny = p + dx, q + dy
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                queue.append((nx, ny, r+1))