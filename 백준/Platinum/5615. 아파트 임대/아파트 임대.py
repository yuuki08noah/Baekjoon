import random
import math
import sys
sys.setrecursionlimit(10**7)

miller_rabin = [2, 7, 61]

def rand():
    return random.randint(1, 10000000)

def power(base, exponent, mod):
    res = 1

    base %= mod
    while exponent > 0:
        if exponent % 2 == 1:
            res = res * base % mod
        exponent = exponent // 2
        base = (base*base)%mod
    return res

def m_r(n, a):
    d = n - 1
    while d%2 == 0:
        d //= 2
    x = power(a, d, n)
    if x==1 or x==n-1:
        return True
    while d != n-1:
        x = power(x, 2, n)
        d*=2
        if x==1:
            return False
        if x==n-1:
            return True
    return False

def isPrime(n):
    if n in miller_rabin:
        return True

    if n==1 or n%2==0:
        return False

    for i in miller_rabin:
        if not m_r(n, i):
            return False

    return True

input = sys.stdin.readline
n = int(input())
l = []
for i in range(100000):
    if isPrime(i):
        l.append(i)

cnt = 0
for i in range(n):
    m = int(input())
    if isPrime(2*m + 1):
        cnt+=1
print(cnt)