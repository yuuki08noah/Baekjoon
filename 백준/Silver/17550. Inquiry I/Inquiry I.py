import sys

input = sys.stdin.readline
s = int(input())
arr = [int(input()) for _ in range(s)]
k = arr[:]
res = 0
arr[0] *= arr[0]
for i in range(1, s):
    k[i] += k[i-1]
    arr[i] = arr[i]*arr[i]+arr[i-1]
for i in range(s):
    res = max(res, arr[i]*(k[-1]-k[i]))
print(res)