import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
cost = []

for i in range(n):
    a, b = map(int, input().split())
    arr.append(a)
    cost.append(b)

result = [0] * (m + 1)

for i in range(n):
    for j in range(m, arr[i]-1, -1):
        result[j] = max(result[j], result[j-arr[i]] + cost[i])

print(max(result))