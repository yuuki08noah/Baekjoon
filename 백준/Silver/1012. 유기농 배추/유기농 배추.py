import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
t = int(input())
for i in range(t):
    m, n, k = map(int, input().split())
    board = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())
        board[y][x] = 1
    
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    def dfs(x, y):
        board[x][y] = 2
        for i in range(4):
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