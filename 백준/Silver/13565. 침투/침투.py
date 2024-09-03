import sys
import math

input = sys.stdin.readline
sys.setrecursionlimit(10**6)  # 재귀 한도 늘리기
k, m = map(int, input().split())
board = []
visited = [[False] * m for _ in range(k)]  # 방문 여부 체크 배열

def dfs(f, n):
    if f == k-1:
        return True
    visited[f][n] = True
    if board[f+1][n] == '0':
        for i in range(n, m):
            if board[f+1][i] == '0' and not visited[f+1][i]:
                if dfs(f+1, i):
                    return True
            if board[f+1][i] == '1':
                break
        for i in range(n-1, -1, -1):
            if board[f + 1][i] == '0' and not visited[f+1][i]:
                if dfs(f + 1, i):
                    return True
            if board[f + 1][i] == '1':
                break

    if f > 0 and board[f-1][n] == '0':
        for i in range(n, m):
            if board[f-1][i] == '0' and not visited[f-1][i]:
                if dfs(f-1, i):
                    return True
            if board[f-1][i] == '1':
                break
        for i in range(n-1, -1, -1):
            if board[f - 1][i] == '0' and not visited[f-1][i]:
                if dfs(f - 1, i):
                    return True
            if board[f - 1][i] == '1':
                break
    return False

for i in range(k):
    board.append(list(map(str, input().strip())))
for i in range(m):
    if board[0][i] == '0' and not visited[0][i]:
        if dfs(0, i):
            print('YES')
            exit()
print('NO')


