import sys
from collections import deque
import heapq

input = sys.stdin.readline
dp = [0, 1]
for i in range(2, 60):
    dp.append(dp[i-1]+dp[i-2])
t = int(input())
for _ in range(t):
    n = int(input())
    res = []
    for i in range(59, 0, -1):
        if dp[i] <= n:
            n -= dp[i]
            res.append(dp[i])
        if n == 0:
            break
    res.reverse()
    print(*res)
