import sys
input = sys.stdin.readline

n, p, q = map(int, input().split())
memo = {0: 1}

def solve(x):
    if x in memo: return memo[x]
    memo[x] = solve(x//p) + solve(x//q)
    return memo[x]

print(solve(n))