import sys

input = sys.stdin.readline

base, year = map(int, input().split())
dp = [0] * (year + 1)
dp[0] = base

for i in range(1, year + 1):
    dp[i] = max(dp[i], dp[i - 1] + dp[i - 1] // 20)
    if i >= 3:
        dp[i] = max(dp[i], dp[i - 3] + dp[i - 3] // 5)
    if i >= 5:
        dp[i] = max(dp[i], dp[i - 5] + (dp[i - 5] * 7) // 20)
print(int(dp[year]))