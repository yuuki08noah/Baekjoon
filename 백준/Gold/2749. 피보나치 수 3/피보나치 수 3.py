import sys

input = sys.stdin.readline
n = int(input())
mod = 10**6
k = mod//10 * 15
fib = [1] * (n % k + 1)
for i in range(3, n % k+1):
    fib[i] = (fib[i - 1] + fib[i - 2])%mod

print(fib[n%k]%(10**6))
