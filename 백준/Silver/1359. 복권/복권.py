import sys
import bisect

input = sys.stdin.readline
n, m, k = map(int, input().split())

def fac(n):
    res = 1
    while n > 1:
        res *= n
        n -= 1
    return res

def nCr(n, r):
    return fac(n)//(fac(n-r)*fac(r))

r = 0
for i in range(k, m+1):
    if n - m < m - k:
        r = 1
        break
    r += nCr(m, i)*nCr(n-m, m-i)/nCr(n, m)
print(r)