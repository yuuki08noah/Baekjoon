import sys
n = int(sys.stdin.readline())

fib = [0, 1]
for j in range(2, n+1):
    fib.append((fib[j - 1] + fib[j - 2])%1000000007)

print(fib[n])
