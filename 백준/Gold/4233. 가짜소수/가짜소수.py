import sys
import math

miller_rabin = [2, 7, 61]
def m_r(n, a):
    d = n - 1
    while d % 2 == 0:
        d //= 2  # n - 1 = 2**s*d
    x = pow(a, d, n)  # a**d (mod n)
    if x == 1 or x == n - 1:  # 위가 1 혹은 mod n이 -1이라면
        return True
    while d != n - 1:  # 제곱을 해주면서 2**s가 될때까지
        x = pow(x, 2, n)
        d *= 2
        if x == n - 1:  # a**{d*2**r}=-1(mod n)이면 True
            return True
    return False


def isPrime(n):
    if n in miller_rabin:
        return True

    if n == 1 or n % 2 == 0:
        return False

    for i in miller_rabin:
        if not m_r(n, i):
            return False

    return True


input = sys.stdin.readline
while True:
    p, a = map(int, input().split())
    if isPrime(p):
        print("no")
        continue
    if p == 0 and a == 0:
        break
    if pow(a, p, p) == a:
        print("yes")
        continue
    print("no")
