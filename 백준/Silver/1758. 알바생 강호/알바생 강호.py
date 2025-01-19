import sys

input = sys.stdin.readline
n = int(input())
arr = sorted([int(input()) for _ in range(n)], reverse=True)
res = 0
for i in range(n):
    res += arr[i] - i if arr[i] - i > 0 else 0
print(res)
