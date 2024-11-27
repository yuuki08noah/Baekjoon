import sys
from collections import deque

input = sys.stdin.readline
p = 1
while True:
    n = int(input())
    if n == 0:
        break
    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * n for _ in range(n)]
    costs = [[10**9] * n for _ in range(n)]
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    queue = deque([(0, 0)])
    costs[0][0] = board[0][0]

    while queue:
        x, y = queue.popleft()
        # if visited[x][y]:
        #     continue
        visited[x][y] = True

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and costs[x][y] + board[nx][ny] < costs[nx][ny]:
                costs[nx][ny] = costs[x][y] + board[nx][ny]
                queue.append((nx, ny))

    print(f"Problem {p}: {costs[-1][-1]}")
    p += 1
