import math
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
dp = [1]
if n==m or m==0:
    print(1)
    exit()
for i in range(2, n+1):
    dp.append((i%10007*dp[i-2]))
res = (dp[n-1]//(dp[n-m-1]*dp[m-1]))%10007
print(res)