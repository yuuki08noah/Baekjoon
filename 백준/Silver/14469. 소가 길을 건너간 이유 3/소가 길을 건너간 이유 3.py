import sys

input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x: (x[0], x[1]))
cost = 0

for k in arr:
    if cost < k[0]:
        cost = k[0] + k[1]
    else:
        cost += k[1]

print(cost)