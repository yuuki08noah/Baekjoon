import math
import sys

input = sys.stdin.readline
t = int(input())
for q in range(t):
    m, n = map(int, input().split())
    dp = [1]
    if n==m or m==0:
        print(1)
        continue
    for i in range(2, n+1):
        dp.append((i*dp[i-2]))
    res = (dp[n-1]//(dp[n-m-1]*dp[m-1]))
    print(res)