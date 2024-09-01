import sys
import math
from bisect import bisect_left

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

x = [arr[0]]
pos = [0] * n
pos[0] = 0

for i in range(1, n):
    if arr[i] > x[-1]:
        x.append(arr[i])
        pos[i] = len(x) - 1
    else:
        idx = bisect_left(x, arr[i])
        x[idx] = arr[i]
        pos[i] = idx

lis_length = len(x)
print(lis_length)

lis = [0] * lis_length
idx = lis_length - 1
for i in range(n - 1, -1, -1):
    if pos[i] == idx:
        lis[idx] = arr[i]
        idx -= 1
print(*lis)
