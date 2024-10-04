import sys
from collections import deque
import heapq

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
benefit, result = 0, 0
for i in range(n-1, -1, -1):
    benefit = max(benefit, arr[i])
    result = max(result, benefit - arr[i])
print(result)