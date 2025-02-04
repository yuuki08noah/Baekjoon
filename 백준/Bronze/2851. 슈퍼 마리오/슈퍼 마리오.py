import sys

input = sys.stdin.readline
arr = [(0, 100)]
for i in range(10):
    n = int(input())
    arr.append((n+arr[-1][0], 100-n-arr[-1][0]))

arr.sort(key=lambda x: (abs(x[1]), -x[0]))
print(arr[0][0])