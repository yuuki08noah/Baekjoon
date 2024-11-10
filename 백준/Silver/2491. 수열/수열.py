import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

m = 1
k = 1
for i in range(len(arr) - 1):
    if arr[i] >= arr[i + 1]:
        k += 1
    else:
        m = max(m, k)
        k = 1
m = max(m, k)
k = 1
for i in range(len(arr) - 1):
    if arr[i] <= arr[i + 1]:
        k += 1
    else:
        m = max(m, k)
        k = 1
m = max(m, k)
print(m)