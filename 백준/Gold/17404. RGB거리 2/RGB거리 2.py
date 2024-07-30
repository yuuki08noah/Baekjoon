import sys

input = sys.stdin.readline
n = int(input())
dp = []
ans = 10**9
I = 10**9

for i in range(n):
    dp.append(list(map(int, input().split())))

for i in range(3):
    arr = [[I, I, I] for _ in range(n)]
    arr[0][i] = dp[0][i]
    for j in range(1, n):
        arr[j][0] = dp[j][0] + min(arr[j-1][1], arr[j-1][2])
        arr[j][1] = dp[j][1] + min(arr[j-1][0], arr[j-1][2])
        arr[j][2] = dp[j][2] + min(arr[j-1][1], arr[j-1][0])
    for c in range(3):
        if i != c:
            ans = min(ans, arr[n-1][c])
print(ans)