import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
length = [1] * n
for i in range(1, n):
    for j in range(i):
        if arr[j] > arr[i]:
            length[i] = max(length[i], length[j] + 1)
print(n - max(length))