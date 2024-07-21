import sys
n = int(sys.stdin.readline())

for i in range(n):
    fib = [0, 1]
    p = int(sys.stdin.readline())
    for j in range(2, 100001):
        fib.append((fib[j - 1] + fib[j - 2]))
        if (fib[j - 1] + fib[j - 2]) == p:
            print(j)
            break
