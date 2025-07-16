import sys
from collections import defaultdict
sys.setrecursionlimit(200000)

input = sys.stdin.readline
sieve = [True] * 10001
primes = []
for i in range(2, 10001):
    if sieve[i]:
        for j in range(i*2, 10001, i):
            sieve[j] = False
for i in range(2, 10001):
    if sieve[i]: primes.append(i)

memo = {}
values = defaultdict(tuple)
diff = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(start, end):
    for x, y in diff:
        nx = x + start
        ny = y + end
        if nx >= 0 and ny < len(primes) and nx <= ny and (nx, ny) not in memo and abs(primes[nx]-primes[ny]) < 1000:
            memo[(nx, ny)] = primes[nx] + primes[ny]
            if values[memo[(nx, ny)]] == ():
                values[memo[(nx, ny)]] = (primes[nx], primes[ny])
            else:
                if abs(values[memo[(nx, ny)]][0]-values[memo[(nx, ny)]][1]) > abs(primes[nx]-primes[ny]):
                    values[memo[(nx, ny)]] = (primes[nx], primes[ny])
            dfs(nx, ny)
dfs(0, 0)
for _ in range(int(input())):
    n = int(input())
    print(*values[n])