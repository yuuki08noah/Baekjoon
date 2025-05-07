import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
tree = {i: [] for i in range(1, n+1)}

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

dp = [[0] * 2 for _ in range(n+1)]
visited = [False] * (n+1)

def tree_dp(u):
    visited[u] = True
    children = tree[u]

    dp[u][0] = 1

    for v in children:
        if not visited[v]:
            tree_dp(v)
            dp[u][1] += dp[v][0]
            dp[u][0] += min(dp[v][0], dp[v][1])

tree_dp(1)
print(min(dp[1][0], dp[1][1]))