import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split())) + [0] * n
r = -100
for i in range(1, n):
    arr[i] += arr[i-1]
for i in range(m-1, n):
    r = max(arr[i]-arr[i-m], r)
# print(arr)
print(r)