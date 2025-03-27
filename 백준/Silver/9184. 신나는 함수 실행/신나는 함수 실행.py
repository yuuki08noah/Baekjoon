import sys

input = sys.stdin.readline

memo = {}

def f(a, b, c):
    if a <= 0 or b <= 0 or c <= 0: return 1
    if a > 20 or b > 20 or c > 20:
        memo[(a, b, c)] = f(20, 20, 20)
        return memo[(a, b, c)]
    if (a, b, c) in memo: return memo[(a, b, c)]
    if a < b < c:
        memo[(a, b, c)] = f(a, b, c-1) + f(a, b-1, c-1) - f(a, b-1, c)
        return memo[(a, b, c)]
    else:
        memo[(a, b, c)] =  f(a - 1, b, c) + f(a - 1, b - 1, c) + f(a - 1, b, c - 1) - f(a - 1, b - 1, c - 1)
        return memo[(a, b, c)]

while True:
    a, b, c = map(int, input().split())
    if a == b == c == -1: break
    print(f'w({a}, {b}, {c}) = {f(a, b, c)}')
