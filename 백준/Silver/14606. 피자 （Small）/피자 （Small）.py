import sys

input = sys.stdin.readline

n = int(input())
dp = [0] * 11
dp[0] = 0
dp[1] = 0
dp[2] = 1
dp[3] = 3
for i in range(4, n + 1):
    for j in range(1, i // 2 + 1):
        dp[i] = max(dp[i], (i - j) * j + dp[i - j] + dp[j])

print(dp[n])