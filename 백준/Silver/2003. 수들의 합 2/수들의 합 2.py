import sys
from decimal import Decimal
import heapq
import decimal
from bisect import bisect_left

input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
start, end = 0, 0
cnt = 0
while start < n and end < n:
    # print(sum(arr[start:end+1]))
    # print(start, end)
    if sum(arr[start:end+1]) == m:
        cnt += 1
        end += 1
    elif sum(arr[start:end+1]) > m:
        start += 1
    elif sum(arr[start:end+1]) < m:
        end += 1
print(cnt)