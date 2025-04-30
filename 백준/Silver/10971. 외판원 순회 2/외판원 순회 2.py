import sys
from copy import copy
from math import inf

input = sys.stdin.readline
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dp = {}

def f(start, last, l):
    if len(l) == 0:
        return graph[last][start] if graph[last][start] != 0 else inf
    key = (frozenset(l), last)
    if key in dp:
        return dp[key]
    k = inf
    for p in l:
        if graph[last][p] == 0: continue
        k = min(k, graph[last][p] + f(start, p, l - {p}))
    dp[key] = k
    return k

res = f(0, 0, frozenset({j for j in range(n) if j != 0}))
print(res)

