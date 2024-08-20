import sys
import math
from bisect import bisect_left

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
dp = [1]
x = [arr[0]]
for i in range(1, n):
    if arr[i] > x[-1]:
        dp.append(dp[-1]+1)
        x.append(arr[i])
    else:
        x[bisect_left(x, arr[i])] = arr[i]
print(len(x))