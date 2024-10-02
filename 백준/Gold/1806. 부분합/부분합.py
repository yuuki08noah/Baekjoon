import sys
from collections import deque
import heapq

sys = sys.stdin.readline
n, s = map(int, input().split())
arr = list(map(int, input().split()))
arr.insert(0, 0)
start, end = 0, 0
for i in range(1, n+1):
    arr[i] += arr[i - 1]
minLen = 10**9
while start <= end and end < n+1:
    if start == end:
        if arr[start] >= s:
            minLen = 1
            break
        end += 1
    elif arr[end] - arr[start] < s:
        end += 1
    else:
        minLen = min(minLen, end - start)
        start += 1
print(minLen if minLen != 10**9 else 0)
