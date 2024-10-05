import sys
from collections import deque
import heapq

input = sys.stdin.readline
n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
cnt = 0
for i in range(m):
    if n >= 200:
        break
    cnt += 1
    n += arr[i]

print(cnt)
