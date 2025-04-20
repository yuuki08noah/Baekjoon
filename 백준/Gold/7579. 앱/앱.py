import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
cost = list(map(int, input().split()))
result = [0] * (sum(cost) + 1)
for i in range(n):
    for j in range(sum(cost), cost[i]-1, -1):
        result[j] = max(result[j], result[j-cost[i]] + arr[i])

for i in range(sum(cost)+1):
    if result[i] >= m:
        print(i)
        break