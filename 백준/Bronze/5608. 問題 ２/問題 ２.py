import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
table = {}
for i in range(n):
    a, b = input().strip().split()
    table[a] = b
m = int(input())
for i in range(m):
    c = input().strip()
    if c in table:
        print(table[c], end='')
    else:
        print(c, end='')