import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
res = 0
while len(arr) != 1:
    max_value = arr.pop()
    min_value = arr.pop(0)
    res += max_value * min_value
    arr.append(max_value + min_value)
    arr.sort()
print(res)