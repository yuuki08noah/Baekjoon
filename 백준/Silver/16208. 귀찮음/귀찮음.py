import bisect
import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
arr = deque(sorted(map(int, input().split())))
res = 0
while len(arr) != 1:
    max_value = arr.pop()
    min_value = arr.popleft()
    res += max_value * min_value
    arr.insert(bisect.bisect_left(arr, max_value + min_value), max_value+min_value)

print(res)