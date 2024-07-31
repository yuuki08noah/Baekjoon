import sys
import math

input = sys.stdin.readline
n, k, mod = map(int, input().split())

def fac(n):
    res = 1
    while n > 1:
        res *= n
        res %= mod
        n -= 1
    return res

def nCr(n, r):
    if n < r:
        return 0
    elif n == r or r == 0:
        return 1
    return fac(n)*pow(fac(r)*fac(n-r), mod-2, mod)

res = 1
while True:
    t = 1
    while True:
        if t * mod > n:
            break
        t *= mod

    if nCr(n//t, k//t)==0:
        res = 0
        break
    if n == n%t and k == k%t:
        break
    res *= nCr(n//t, k//t)%mod
    n %= t
    k %= t

print(res%mod)