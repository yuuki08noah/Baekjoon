import sys
import math

input = sys.stdin.readline
r = int(input())
n = int(input())
r -= 1
n -= 1

def fac(n):
    res = 1
    while n > 1:
        res *= n
        res %= 10**9+7
        n-=1
    return res
res = (fac(n)*pow(fac(n-r), 10**9+5, 10**9+7)*pow(fac(r), 10**9+5, 10**9+7))%(10**9+7)
print(res)