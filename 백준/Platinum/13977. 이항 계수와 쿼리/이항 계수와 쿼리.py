import sys
import math

input = sys.stdin.readline
t = int(input())
arr = []
fac = [1, 1]
for _ in range(t):
    n, r = map(int, input().split())
    arr.append([n, r])
for i in range(2, max(map(max, arr))+1):
    fac.append((fac[-1]*i)%(10**9+7))

for i in arr:
    if i[1] == 0:
        print(1)
        continue
    if i[0] == 1:
        print(1)
        continue
    res = (fac[i[0]]*pow(fac[i[0]-i[1]]*fac[i[1]], 10**9+5, 10**9+7))%(10**9+7)
    print(res)