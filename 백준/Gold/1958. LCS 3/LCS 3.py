import sys
from collections import deque
import heapq

input = sys.stdin.readline
a = input().strip()
b = input().strip()
c = input().strip()

board = [[[0] * (len(c)+1) for _ in range(len(b)+1)] for i in range(len(a)+1)]
for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        for k in range(1, len(c)+1):
            if a[i-1] == b[j-1] == c[k-1]:
                board[i][j][k] = board[i-1][j-1][k-1] + 1
            else:
                board[i][j][k] = max(board[i-1][j][k], board[i][j-1][k], board[i][j][k-1])
print(board[-1][-1][-1])