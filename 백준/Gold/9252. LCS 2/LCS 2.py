import sys
from collections import deque

input = sys.stdin.readline
str1 = input().strip()
str2 = input().strip()

board = [[0] * (len(str2)+1) for i in range(len(str1)+1)]
for i in range(1, len(str1)+1):
    for j in range(1, len(str2)+1):
        previous = max(board[i-1][j], board[i][j-1])
        if str1[i-1] == str2[j-1]:
            board[i][j] = board[i - 1][j - 1] + 1
        else:
            board[i][j] = previous

queue = deque([(len(str1), len(str2))])
dx = [0, -1]
dy = [-1, 0]
cstr = []

while queue:
    x, y = queue.popleft()
    temp = []
    for i in range(2):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < len(str1)+1 and 0 <= ny < len(str2)+1:
            temp.append((nx, ny, board[nx][ny]))
    temp.sort(key=lambda k: -k[2])
    if len(temp) > 0:
        if board[temp[0][0]][temp[0][1]] != board[x][y]:
            queue.append((x - 1, y - 1))
            cstr.append(str1[x-1])
        else:
            queue.append((temp[0][0], temp[0][1]))
cstr.reverse()
print(board[-1][-1])
print(*cstr, sep='')
