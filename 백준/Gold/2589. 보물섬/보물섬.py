import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]
d = 0

for i in range(n):
    for j in range(m):
        if arr[i][j] == 'L':
            visited = [[False] * m for _ in range(n)]
            queue = deque([(i, j, 0)])
            while queue:
                x, y, depth = queue.popleft()
                if visited[x][y]: continue
                d = max(d, depth)
                visited[x][y] = True
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
                    if not visited[nx][ny] and arr[nx][ny] == 'L':
                        queue.append((nx, ny, depth + 1))

# print(*visited, sep='\n')
print(d)
