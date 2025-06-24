import sys

input = sys.stdin.readline

n = int(input())
costs = []

for i in range(n):
    costs.append(list(map(lambda x: int(x) if int(x) != 0 else 10**9, input().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            costs[i][j] = min(costs[i][j], costs[i][k] + costs[k][j])

# print(costs)
for i in range(n):
    for j in range(n):
        if costs[i][j] == 10**9:
            costs[i][j] = 0
        else:
            costs[i][j] = 1

for i in range(n):
    print(*costs[i])