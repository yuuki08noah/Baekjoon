import sys


def fibonacci(n):
    if n <= 1:
        return n
    fib = [1, 3]

    for i in range(3, n + 1):
        fib.append(fib[-1] + 2*fib[-2])

    return fib[-1]

input = sys.stdin.readline
while True:
    try:
        t = int(input())
        if t == 0:
            print(1)
            continue
        print(fibonacci(t))
    except:
        break