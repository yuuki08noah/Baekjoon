import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
l = []
for i in range(n):
    s = sorted(list(input().strip()))
    if s in l: continue
    l.append(s)
print(len(l))