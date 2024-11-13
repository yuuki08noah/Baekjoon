import sys
from collections import deque

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    cnt = 0
    n, m = map(int, input().split())
    board = list(list(map(str, input().strip())) for _ in range(n))
    for i in range(n):
        for j in range(m):
            if board[i][j] == '#':
                queue = deque([(i, j)])
                while queue:
                    x, y = queue.popleft()
                    if board[x][y] != '#':
                        continue
                    board[x][y] = '.'
                    for nx, ny in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
                        if 0 <= nx < n and 0 <= ny < m:
                            if board[nx][ny] == '#':
                                queue.append((nx, ny))
                cnt += 1
    print(cnt)