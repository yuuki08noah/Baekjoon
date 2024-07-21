import sys
n = int(sys.stdin.readline())

for i in range(n):
    fib = [0, 1]
    p, q = map(int, sys.stdin.readline().split())
    for j in range(2, p+1):
        fib.append((fib[j - 1] + fib[j - 2])%q)
    print(f"Case #{i+1}: {fib[p]%q}")