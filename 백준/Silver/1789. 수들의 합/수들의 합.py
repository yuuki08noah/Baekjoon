import sys
from collections import deque
import heapq

input = sys.stdin.readline
n = int(input())
res = 0
for i in range(1, n+1):
    if n - i >= i + 1:
        n -= i
        res += 1
    else:
        res += 1
        break
print(res)