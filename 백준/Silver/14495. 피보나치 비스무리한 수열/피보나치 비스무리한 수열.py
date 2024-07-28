import sys

dp = [1, 1, 1]
input = sys.stdin.readline
n = int(input())

for i in range(3, n+1):
    dp.append(dp[i-1]+dp[i-3])
print(dp[n-1])
