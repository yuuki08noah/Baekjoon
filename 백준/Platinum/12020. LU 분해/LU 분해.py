import sys

input = sys.stdin.readline
n = int(input())
equations = []
for i in range(n):
    equations.append(list(map(int, input().split())))

U = [row[:] for row in equations]
L = [[0.0] * n for _ in range(n)]
for i in range(n):
    L[i][i] = 1.0

for t in range(1, n):
    if U[t-1][t-1] == 0:
        print(-1)
        exit()
    for i in range(t, n):
        mul = U[i][t-1] / U[t-1][t-1]
        L[i][t-1] = mul
        for j in range(t-1, n):
            U[i][j] -= mul * U[t-1][j]

for i in range(n):
    if U[i][i] == 0:
        print(-1)
        exit()

for row in L:
    print(' '.join(f"{elem:.3f}" for elem in row))
for row in U:
    print(' '.join(f"{elem:.3f}" for elem in row))
