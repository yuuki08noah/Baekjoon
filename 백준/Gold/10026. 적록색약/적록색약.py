import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
board = [list(input().strip()) for _ in range(n)]
visitedA = [[False] * n for _ in range(n)]
visitedB = [[False] * n for _ in range(n)]
notR, R = 0, 0
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

for i in range(n):
    for j in range(n):
        if board[i][j] == 'R' and not visitedA[i][j]:
            notR += 1
            queue = deque([(i, j)])
            while queue:
                x, y = queue.popleft()
                if visitedA[x][y]:
                    continue
                visitedA[x][y] = True
                for o, p in zip(dx, dy):
                    nx, ny = x + o, y + p
                    if 0 <= nx < n and 0 <= ny < n:
                        if board[nx][ny] == 'R':
                            queue.append((nx, ny))
        if (board[i][j] == 'G' or board[i][j] == 'R') and not visitedB[i][j]:
            R += 1
            queue = deque([(i, j)])
            while queue:
                x, y = queue.popleft()
                if visitedB[x][y]:
                    continue
                visitedB[x][y] = True
                for o, p in zip(dx, dy):
                    nx, ny = x + o, y + p
                    if 0 <= nx < n and 0 <= ny < n:
                        if board[nx][ny] == 'R' or board[nx][ny] == 'G':
                            queue.append((nx, ny))
        if board[i][j] == 'B' and not visitedA[i][j] and not visitedB[i][j]:
            R += 1
            notR += 1
            queue = deque([(i, j)])
            while queue:
                x, y = queue.popleft()
                if visitedB[x][y] and visitedA[x][y]:
                    continue
                visitedA[x][y] = True
                visitedB[x][y] = True
                for o, p in zip(dx, dy):
                    nx, ny = x + o, y + p
                    if 0 <= nx < n and 0 <= ny < n:
                        if board[nx][ny] == 'B':
                            queue.append((nx, ny))
        if board[i][j] == 'G' and not visitedA[i][j]:
            notR += 1
            queue = deque([(i, j)])
            while queue:
                x, y = queue.popleft()
                if visitedA[x][y]:
                    continue
                visitedA[x][y] = True
                for o, p in zip(dx, dy):
                    nx, ny = x + o, y + p
                    if 0 <= nx < n and 0 <= ny < n:
                        if board[nx][ny] == 'G':
                            queue.append((nx, ny))
print(notR, R)