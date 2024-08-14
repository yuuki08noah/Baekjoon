import sys
import math

input = sys.stdin.readline
arr = []

while True:
    n = int(input())
    if n == -1:
        break
    arr.append(n)

dp = [1]
for i in range(1, max(arr)+1):
    dp.append((dp[int(i - math.sqrt(i))] + dp[int(math.log(i))] + dp[int(i*math.sin(i)**2)])%1000000)
for i in arr:
    print(dp[i])
