import sys
from decimal import Decimal
import heapq
import decimal

input = sys.stdin.readline
n = int(input())
arr = sorted(list(map(int, input().split())))
start, end = 0, n-1
ans = abs(arr[start] + arr[end])
res = [arr[start], arr[end]]
while True:
    if ans > abs(arr[start] + arr[end]):
        res = [arr[start], arr[end]]
        ans = abs(arr[start] + arr[end])
    sum = arr[start] + arr[end]
    if sum < 0:
        start += 1
    elif sum > 0:
        end -= 1
    if start == end or sum == 0:
        break
print(*res)
