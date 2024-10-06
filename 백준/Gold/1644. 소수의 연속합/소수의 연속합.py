import sys

input = sys.stdin.readline
n = int(input())
primes = []
sieve = [True] * 4000001
for i in range(2, 2001):
    for j in range(i*i, 4000001, i):
        sieve[j] = False
for i in range(2, 4000001):
    if sieve[i]:
        primes.append(i)

start, end, c = 0, 0, 0
def sum(start, end):
    res = 0
    for i in range(start, end+1):
        res += primes[i]
    return res

while end < len(primes) and primes[end] <= n:
    s = sum(start, end)
    if s == n:
        c += 1
        end += 1
    elif s < n:
        end += 1
    else:
        start += 1
print(c)
