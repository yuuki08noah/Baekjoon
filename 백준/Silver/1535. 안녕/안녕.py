import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
values = list(map(int, input().split()))
dp = [0] * 101

for i in range(n):
    for j in range(100, arr[i], -1):
        dp[j] = max(dp[j - arr[i]]+values[i], dp[j])
print(max(dp))