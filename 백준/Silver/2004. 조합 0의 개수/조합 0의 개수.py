import random
import math
import sys
import decimal

def fac(n, t):
    res = 0
    while True:
        res += n // t
        if n // t == 0:
            break
        n //= t
    return res

input = sys.stdin.readline
n, m = map(int, input().split())
# print(fac(n))
print(min(fac(n, 2) - fac(n-m, 2) - fac(m, 2), fac(n, 5)-fac(n-m, 5)-fac(m, 5)))