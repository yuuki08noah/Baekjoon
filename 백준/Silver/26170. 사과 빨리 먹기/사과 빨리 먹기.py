import sys
from collections import deque

input = sys.stdin.readline
graph = [list(map(int, input().split())) for _ in range(5)]
visited = [[0] * 5 for _ in range(5)]
r, c = map(int, input().split())
res = 10**9

def dfs(x, y, d, l, li):
    global res
    if visited[x][y] == -1: return
    
    if graph[x][y] == 1 and (x, y) not in li:
        l += 1
        li.append((x, y))
        if l == 3:
            res = min(res, d)
            visited[x][y] = 0  # 백트래킹 추가
            li.pop()
            return
    
    visited[x][y] = -1  # 방문 처리

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 5 and 0 <= ny < 5 and visited[nx][ny] != -1 and graph[nx][ny] != -1:
            dfs(nx, ny, d + 1, l, li)

    visited[x][y] = 0  # 백트래킹 추가
    if li and li[-1] == (x, y):  
        li.pop()

dfs(r, c, 0, 0, [])
print(res if res != 10**9 else -1)