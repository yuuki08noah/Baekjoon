import sys

dp = [1, 1, 2, 4, 7, 13]

input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))

for i in range(6, max(arr)+1):
    dp.append((dp[i-3]+dp[i-2]+dp[i-1])%1000000009)

for i in arr:
    print(dp[i]%1000000009)


