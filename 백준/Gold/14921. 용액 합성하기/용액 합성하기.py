import sys
from decimal import Decimal
import heapq
import decimal

input = sys.stdin.readline
n = int(input().strip())
arr = sorted(list(map(int, input().strip().split())))
start, end = 0, n-1
ans = abs(arr[start] + arr[end])
res = [arr[start], arr[end]]
while True:
    if ans > abs(arr[start] + arr[end]):
        res = [arr[start], arr[end]]
        ans = abs(arr[start] + arr[end])
    s = arr[start] + arr[end]
    if s < 0:
        start += 1
    elif s > 0:
        end -= 1
    if start == end or s == 0:
        break
print(sum(res))
