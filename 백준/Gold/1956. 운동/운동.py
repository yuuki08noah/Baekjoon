import sys

input = sys.stdin.readline

n, m = map(int, input().split())
costs = {i:[10**9 if i != j else 0 for j in range(n+1)] for i in range(1, n+1)}
res = 10**9

for i in range(m):
    a, b, c = map(int, input().split())
    costs[a][b] = min(costs[a][b], c)

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                costs[i][j] = 0
                continue
            costs[i][j] = min(costs[i][j], costs[i][k] + costs[k][j])
            res = min(res, costs[i][j] + costs[j][i])

print(res if res != 10**9 else -1)