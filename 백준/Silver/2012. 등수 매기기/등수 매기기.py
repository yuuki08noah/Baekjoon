import decimal
import sys
import math

input = sys.stdin.readline
n = int(input())
arr = []
temp = [i for i in range(1, n+1)]
for i in range(n):
    arr.append(int(input()))

arr.sort()
cnt = 0
for i in range(len(arr)):
    cnt += abs(temp[i] - arr[i])

print(cnt)