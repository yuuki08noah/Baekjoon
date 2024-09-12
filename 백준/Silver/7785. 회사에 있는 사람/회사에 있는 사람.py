import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
table = {}
for i in range(n):
    name, cmd = input().strip().split()
    if name not in table:
        table.update({name: cmd})
    else:
        table[name] = cmd

sorted_ = sorted(table.items(), reverse=True)
for tb in sorted_:
    if tb[1] == 'enter':
        print(tb[0])
    else:
        continue
