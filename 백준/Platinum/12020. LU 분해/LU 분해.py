import sys

input = sys.stdin.readline
n = int(input())
equations = []
for i in range(n):
    equations.append(list(map(int, input().split())))

U = []
L = [[0.0] * n for _ in range(n)]
for i in range(n):
    L[i][i] = 1.0

U.append(equations[0])
try:
    for t in range(1, n):
        mul = equations[t][t-1] / equations[t-1][t-1]
        u_temp = []
        for j in range(n):
            u_temp.append(equations[t][j] - mul * equations[t-1][j])
            equations[t][j] -= mul * equations[t-1][j]
        for j in range(t):
            L[t][j] = mul
        U.append(u_temp)
    for i in range(n):
        if U[i][i] == 0:
            print(-1)
            exit()
    for i in range(n):
        for j in range(n):
            print(f"{L[i][j]:.3f}", end=' ')
        print()
    for i in range(n):
        for j in range(n):
            print(f"{U[i][j]:.3f}", end=' ')
        print()
except ZeroDivisionError:
    print("-1")
