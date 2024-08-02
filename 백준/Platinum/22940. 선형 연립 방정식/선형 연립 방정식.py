import math
import sys
import heapq

input = sys.stdin.readline
n = int(input())
equations = []
for i in range(n):
    equations.append(list(map(int, input().split())))
for t in range(n-1):
    for i in range(t, n-1):
        mul = equations[i+1][t] / equations[t][t]
        for j in range(n+1):
            equations[i+1][j] -= mul * equations[t][j]
# print(equations)
res = []
res.append(equations[-1][-1]/equations[-1][-2] if equations[-1][-2] != 0 else 1)
idx = 0
for t in range(n-1, 0, -1):
    # print(equations)
    for i in range(0, t):
        equations[i][-1] -= equations[i][t]*res[-1]
    if equations[t-1][t-1] == 0 and equations[t-1][-1] == 0:
        res.append(1)
    else:
        res.append(equations[t-1][-1]/equations[t-1][t-1])
    # print(res)
    idx += 1
for i in range(len(res)-1, -1, -1):
    print(int(round(res[i])), end=' ')
