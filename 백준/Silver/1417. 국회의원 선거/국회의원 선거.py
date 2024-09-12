import sys
from collections import deque
import heapq

input = sys.stdin.readline
n = int(input())
dasom = int(input())
other = []
for i in range(n-1):
    other.append(int(input()))
cnt = 0
if n > 1:
    while dasom <= max(other):
        dasom += 1
        other[other.index(max(other))] -= 1
        cnt += 1
print(cnt)
