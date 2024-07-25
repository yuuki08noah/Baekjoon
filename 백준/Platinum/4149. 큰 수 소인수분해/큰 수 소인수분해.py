import random
import math
import sys
sys.setrecursionlimit(10**7)

miller_rabin = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71]

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

def abs(n):
    if n<0:
        return -n
    else:
        return n
def rec(n, list):
    if n == 1:
        return
    if n % 2 == 0:
        list.append(2)
        rec(n//2, list)
        return
    if isPrime(n):
        list.append(n)
        return
    g = n
    def f(i):
        return (c + (i*i)%n)%n
    while True:
        if g==n:
            a = b = rand() % (n-2) + 2
            c = rand() % 20 + 1
        a = f(a)
        b = f(f(b))
        g = math.gcd(abs(a-b), n)
        if g!=1:
            break
    rec(g, list)
    rec(n // g, list)
    
input = sys.stdin.readline
n = int(input())
l = []
rec(n, l)
l.sort()
for i in l:
    print(i)