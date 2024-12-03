import sys
from decimal import Decimal

input = sys.stdin.readline
n, m = map(int, input().split())
per = (m*100 / n)

start, end = 0, 10**18
res = 10**18

while start <= end:
    mid = (start + end) // 2
    if (m + mid)*100 // (n + mid) > per:
        res = min(res, mid)
        end = mid - 1
    else:
        start = mid + 1

print(res if res != 10**18 else -1)
