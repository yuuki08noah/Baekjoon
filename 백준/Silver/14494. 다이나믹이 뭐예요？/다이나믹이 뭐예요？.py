import sys

input = sys.stdin.readline
n, m = map(int, input().split())
dp = [[0] * m for _ in range(n)]
dp[0][0] = 1
for i in range(n):
    for j in range(m):
        if i > 0 and j > 0:
            dp[i][j] += dp[i-1][j-1]
        if i > 0:
            dp[i][j] += dp[i-1][j]
        if j > 0:
            dp[i][j] += dp[i][j-1]
        dp[i][j] %= 10**9+7

print(dp[n-1][m-1])