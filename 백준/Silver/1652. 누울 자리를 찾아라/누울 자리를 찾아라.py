import sys
import math

input = sys.stdin.readline
n = int(input())
board = [list(map(str, input().strip())) for _ in range(n)]
garo = 0
sero = 0
for k in board:
    cnt = 0
    for j in k:
        if j == '.':
            cnt += 1
        else:
            cnt = 0
        if cnt == 2:
            garo += 1

for k in [list(x) for x in zip(*board)]:
    cnt = 0
    for j in k:
        if j == '.':
            cnt += 1
        else:
            cnt = 0
        if cnt == 2:
            sero += 1
print(garo, sero)
