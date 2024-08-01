import random
import math
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
primes = [False for _ in range(m-n+1)]
for i in range(2, int(math.sqrt(m)+1)):
    pow = i * i
    start = n // pow
    if n % pow != 0:
        start += 1
    for j in range(start, m // pow+1):
        primes[j*pow-m] = True

print(primes.count(False))