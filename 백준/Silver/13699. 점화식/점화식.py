import sys

input = sys.stdin.readline
n = int(input())
dp = [1]
for i in range(0, n):
    temp = 0
    k = 0
    for j in range(i, -1, -1):
        temp += dp[j]*dp[k]
        k += 1
    dp.append(temp)
print(dp[-1])