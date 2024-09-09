import sys
from collections import deque
import heapq

input = sys.stdin.readline
n = int(input())
table = {}
for i in range(n):
    str = input()
    if str not in table:
        table.update({str: 1})
    else:
        table[str] += 1
sorted_table = sorted(table.items(), key=lambda x: (-x[1], x[0]))
print(sorted_table[0][0])