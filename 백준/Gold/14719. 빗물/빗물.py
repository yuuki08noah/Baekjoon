import sys
input = sys.stdin.readline

x, y = map(int, input().split())
walls = list(map(int, input().split()))
board = []
for j in range(x):
    temp = []
    for i in range(y):
        if walls[i]>=1:
            temp.append(1)
            walls[i]-=1
        else:
            temp.append(0)
    board.append(temp)

res = 0
for i in range(len(board)):
    t = 2
    cnt = 0
    for j in range(len(board[i])):
        if t==2 and board[i][j] == 1:
            t=0
        elif t==0 and board[i][j]==0 and (j!=0 or j!=len(board[i])-1):
            t=1
            cnt+=1
        elif t==1 and board[i][j]==0 and (j!=0 or j!=len(board[i])-1):
            cnt+=1
        elif t==1 and board[i][j]==1:
            res+=cnt
            cnt=0
            t=1
    #     print(cnt, end=' ')
    # print()
print(res)
