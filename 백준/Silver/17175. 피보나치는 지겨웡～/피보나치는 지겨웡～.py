import decimal
import sys
import math

sys.set_int_max_str_digits(100000000)
input = sys.stdin.readline
dp = [1, 1]
n = int(input())
for i in range(2, n + 2):
    dp.append((dp[i-1]+dp[i-2]+1)%1000000007)
print(dp[n])