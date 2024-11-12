import sys

input = sys.stdin.readline
mod = 10007
n, r = map(int, input().split())
if r == 0:
    print(1)
    exit()
dp = [[0] * min(i + 1, r + 1) for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, min(i + 1, r + 1)):
        if j == 1:
            dp[i][j] = i
            continue
        elif j == i:
            dp[i][j] = 1
            continue
        dp[i][j] = (dp[i-1][j] + dp[i-1][j-1]) % mod

print(dp[n][r] % mod)