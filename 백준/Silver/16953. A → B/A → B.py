import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
res = 1

while m != n:
    temp = m
    if m % 2 == 0:
        m //= 2
    elif m % 10 == 1:
        m //= 10
    if temp == m:
        print(-1)
        exit()
    res += 1
print(res)
