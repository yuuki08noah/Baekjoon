import copy
import sys

input = sys.stdin.readline
arr = list(map(int, list(input().strip())))
n = len(arr)
arr.insert(0, 0)
l = 0
for i in range(1, n+1):
    arr[i] += arr[i-1]

for i in range(0, n):
    for j in range(1, n):
        if i+j*2 >= n + 1: continue
        if arr[i+j] - arr[i] == arr[i+j*2] - arr[j+i]:
            l = max(j*2, l)
print(l)