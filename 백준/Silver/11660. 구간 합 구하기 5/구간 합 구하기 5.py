import sys

input = sys.stdin.readline
n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

for i in range(1, n):
    board[0][i] += board[0][i-1]
    board[i][0] += board[i-1][0]

for i in range(1, n):
    for j in range(1, n):
        board[i][j] += board[i][j-1] + board[i-1][j] - board[i-1][j-1]

for i in range(m):
    temp = list(map(int, input().split()))
    res = board[temp[2]-1][temp[3]-1]
    if temp[1]-2 >= 0:
        res -= board[temp[2]-1][temp[1]-2]
    if temp[0]-2 >= 0:
        res -= board[temp[0]-2][temp[3]-1]
    if temp[1]-2 >= 0 and temp[0]-2 >= 0:
        res += board[temp[0]-2][temp[1]-2]
    print(res)