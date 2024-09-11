import sys
from collections import deque
import heapq

input = sys.stdin.readline
a = int(input())
k = a // 300
a %= 300
l = a // 60
a %= 60
m = a // 10
a %= 10
if a > 0:
    print(-1)
else:
    print(k, l, m)