import sys

input = sys.stdin.readline
n, k = map(int, input().split())
arr = [0]
res = 0
for i in range(n):
    arr.append(arr[-1] + int(input()))

for i in range(1, n+1-k):
    res = max(arr[i+k]-arr[i-0], res)
print(res)