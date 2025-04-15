import sys

input = sys.stdin.readline
t = int(input())
matrix = [tuple(map(int, input().split())) for _ in range(t)]
dp = [[0] * (t+1) for _ in range(t+1)]

for j in range(1, t):
    for i in range(t):
        if i + j == t: break

        dp[i][i+j] = 10**9
        for k in range(i, i+j):
            dp[i][i+j] = min(dp[i][i+j],
                             dp[i][k]+dp[k+1][i+j] + matrix[i][0] * matrix[k][1] * matrix[i+j][1])
print(dp[0][t-1])