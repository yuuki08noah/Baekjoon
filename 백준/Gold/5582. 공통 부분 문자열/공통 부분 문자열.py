import sys
from collections import deque
import heapq

input = sys.stdin.readline
a = input().strip()
b = input().strip()

board = [[0] * (len(b)+1) for _ in range(len(a)+1)]
m = 0
for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]:
            board[i][j] = board[i-1][j-1] + 1
            m = max(board[i][j], m)
        else:
            board[i][j] = 0
print(m)