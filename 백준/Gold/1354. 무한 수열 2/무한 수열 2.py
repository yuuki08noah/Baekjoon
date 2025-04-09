import sys
input = sys.stdin.readline

n, p, q, k, l = map(int, input().split())
memo = {0: 1}

def solve(x):
    if x <= 0:
        return 1
    if x in memo: return memo[x]
    memo[x] = solve(x//p - k) + solve(x//q - l)
    return memo[x]

print(solve(n))