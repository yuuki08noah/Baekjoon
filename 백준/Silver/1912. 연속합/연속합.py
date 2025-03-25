import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
res = [arr[0]]
for i in range(1, n):
    if res[-1] + arr[i] > arr[i]:
        res.append(arr[i]+res[-1])
    else:
        res.append(arr[i])
print(max(res))