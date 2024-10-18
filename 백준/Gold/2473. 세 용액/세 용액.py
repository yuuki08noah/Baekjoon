import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
arr = sorted(list(map(int, input().rstrip().split())))
r = []
res = 10000000000000
for i in range(len(arr)):
    start, end = 0, n - 1
    while start < end:
        if start == i:
            start += 1
            continue
        elif end == i:
            end -= 1
            continue
        t = arr[start] + arr[end] + arr[i]
        if abs(t) < abs(res):
            res = t
            r = [arr[start], arr[end], arr[i]]

        if t > 0:
            end -= 1
        elif t < 0:
            start += 1
        else:
            break

print(*sorted(r))