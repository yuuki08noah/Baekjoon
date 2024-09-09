import sys
from collections import deque
import heapq

input = sys.stdin.readline
n = int(input())
arr = []
s = 0
for i in range(n):
    arr.append(list(map(float, input().split())))
arr.append(arr[0])
for i in range(n):
    s += arr[i][0] * arr[i+1][1]
    s -= arr[i+1][0] * arr[i][1]
print(f"{abs(s)/2:.1f}")
