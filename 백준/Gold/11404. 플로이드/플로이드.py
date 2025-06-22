import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
costs = {i:[10**9 if i != j else 0 for j in range(n+1)] for i in range(1, n+1)}

for i in range(m):
    a, b, c = map(int, input().split())
    costs[a][b] = min(costs[a][b], c)

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            costs[i][j] = min(costs[i][j], costs[i][k] + costs[k][j])

for i in range(1, n+1):
    for j in range(1, n+1):
        if costs[i][j] == 10**9:
            costs[i][j] = 0

for i in range(1, n+1):
    print(*costs[i][1:])