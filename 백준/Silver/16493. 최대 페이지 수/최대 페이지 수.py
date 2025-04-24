import sys

input = sys.stdin.readline
m, n = map(int, input().split())
arr = []
values = []
for i in range(n):
    a, b = map(int, input().split())
    arr.append(a)
    values.append(b)
dp = [0] * (m+1)

for i in range(n):
    for j in range(m, arr[i]-1, -1):
        dp[j] = max(dp[j - arr[i]]+values[i], dp[j])
print(max(dp))