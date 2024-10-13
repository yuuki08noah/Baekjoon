import sys
from collections import deque
import heapq

input = sys.stdin.readline
n = int(input())
arr = {}
for i in range(n):
    str_ = input().strip().split(".")[1]
    if str_ in arr:
        arr[str_] += 1
    else:
        arr[str_] = 1

sorte = sorted(arr)
for i in sorte:
    print(i, arr[i])