import sys

input = sys.stdin.readline
n, k = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

for i in range(1, k):
    board[0][i] += board[0][i-1]
for i in range(1, n):
    board[i][0] += board[i-1][0]

for i in range(1, n):
    for j in range(1, k):
        board[i][j] += board[i][j-1] + board[i-1][j] - board[i-1][j-1]

m = int(input())
for i in range(m):
    temp = list(map(int, input().split()))
    temp[0] -= 1
    temp[1] -= 1
    temp[2] -= 1
    temp[3] -= 1
    res = board[temp[2]][temp[3]]
    if temp[1]-1 >= 0:
        res -= board[temp[2]][temp[1]-1]
    if temp[0]-1 >= 0:
        res -= board[temp[0]-1][temp[3]]
    if temp[1]-1 >= 0 and temp[0]-1 >= 0:
        res += board[temp[0]-1][temp[1]-1]
    print(res)