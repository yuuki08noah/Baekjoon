import random
import math
import sys
import decimal

sys.setrecursionlimit(10**7)


def power(base, exponent, mod):
    res = 1

    base %= mod
    while exponent > 0:
        if exponent % 2 == 1:
            res = res * base % mod
        exponent = exponent // 2
        base = (base*base)%mod
    return res

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    a, n, p = map(int, input().split())
    fact = [1]
    for i in range(2, n+1):
        fact.append(fact[i-2]*i)
    print(f'Case #{_+1}: {pow(a, fact[n-1], p)}')