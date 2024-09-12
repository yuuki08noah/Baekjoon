import sys
from collections import deque
import heapq

input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
for i in range(m):
    x = heapq.heappop(arr)
    y = heapq.heappop(arr)
    heapq.heappush(arr, x + y)
    heapq.heappush(arr, x + y)
print(sum(arr))