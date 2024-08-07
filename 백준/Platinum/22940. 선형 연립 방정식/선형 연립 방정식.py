import math
import sys

input = sys.stdin.readline
n = int(input())
equations = []
for i in range(n):
    equations.append(list(map(int, input().split())))
    
for t in range(n-1): # 가우스 소거법
    for i in range(t, n-1):
        mul = equations[i+1][t] / equations[t][t]
        for j in range(n+1):
            equations[i+1][j] -= mul * equations[t][j]

res = [equations[-1][-1]/equations[-1][-2]]
idx = 0
for t in range(n-1, 0, -1):
    for i in range(0, t):
        equations[i][-1] -= equations[i][t]*res[-1]
    res.append(equations[t-1][-1]/equations[t-1][t-1])
    idx += 1

for i in range(len(res)-1, -1, -1):
    print(int(round(res[i])), end=' ')
