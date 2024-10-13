import sys
from collections import deque
import heapq

input = sys.stdin.readline
n = int(input())
data = []
def num(str):
    res = 0
    for i in range(len(str)):
        if 48 <= ord(str[i]) <= 57:
            res += int(str[i])
    return res
for i in range(n):
    typ = input().strip()
    data.append((len(typ), num(typ), typ))

data.sort(key=lambda x: (x[0], x[1], x[2]))
for i in range(n):
    print(data[i][2])
