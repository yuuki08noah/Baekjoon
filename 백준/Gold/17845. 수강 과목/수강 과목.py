import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
cost = []

for i in range(m):
    a, b = map(int, input().split())
    arr.append(b)
    cost.append(a)

result = [0] * (n + 1)

for i in range(m):
    for j in range(n, arr[i]-1, -1):
        result[j] = max(result[j], result[j-arr[i]] + cost[i])

print(max(result))