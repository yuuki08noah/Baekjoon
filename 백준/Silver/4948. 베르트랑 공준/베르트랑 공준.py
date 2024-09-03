import sys
import math

input = sys.stdin.readline
primes = [True] * 250000
primes[0] = primes[1] = False
for i in range(2, int(math.sqrt(250000))):
    if primes[i]:
        for j in range(i*i, 250000, i):
            primes[j] = False
while True:
    n = int(input())
    if n == 0:
        break
    print(primes[n+1:2*n+1].count(True))