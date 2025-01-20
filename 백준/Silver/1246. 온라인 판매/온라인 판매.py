import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = sorted([int(input()) for _ in range(m)])
mc = 0
mk = 0
for i in range(m):
    if mc <= arr[i]*min(m - i, n):
        mk = arr[i]
        mc = arr[i]*min(m - i, n)
print(mk, mc)