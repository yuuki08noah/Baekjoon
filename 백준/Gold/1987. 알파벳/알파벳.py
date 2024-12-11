import sys
import copy
from collections import deque

input = sys.stdin.readline

# sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
board = [list(map(str, input())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
arr = [0] * 26
cnt = 0


def dfs(a, b, depth):
    # print(*arr)
    global cnt
    cnt = max(cnt, depth)
    visited[a][b] = True
    for x, y in [1, 0], [-1, 0], [0, -1], [0, 1]:
        nx, ny = a + x, b + y
        if 0 <= nx < n and 0 <= ny < m:
            if not arr[ord(board[nx][ny])-65]:
                arr[ord(board[nx][ny])-65] += 1
                dfs(nx, ny, depth + 1)
                arr[ord(board[nx][ny])-65] -= 1


arr[ord(board[0][0]) - 65] += 1
dfs(0, 0, 1)
print(cnt)