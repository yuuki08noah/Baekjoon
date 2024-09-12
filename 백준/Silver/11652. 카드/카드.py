import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
table = {}
for i in range(n):
    c = int(input())
    if c not in table:
        table.update({c: 1})
    else:
        table[c] += 1

table = sorted(table.items(), key=lambda x: (x[1], -x[0]))
print(table[-1][0])