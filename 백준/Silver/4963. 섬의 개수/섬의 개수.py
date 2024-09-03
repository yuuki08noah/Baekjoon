import sys
import math
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

while True:
    m, n = map(int, input().split())
    if m == 0 and n == 0:
        break
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))

    dx = [-1, 0, 0, 1, 1, -1, -1, 1]
    dy = [0, -1, 1, 0, 1, -1, 1, -1]

    def dfs(x, y):
        board[x][y] = 2
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not board[nx][ny] == 2:
                if board[nx][ny] == 1:
                    dfs(nx, ny)


    cnt = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 1:
                board[i][j] = 2
                cnt += 1
                dfs(i, j)

    print(cnt)