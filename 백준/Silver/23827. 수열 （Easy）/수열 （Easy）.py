import copy
import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
l = copy.deepcopy(arr)
s = 0
for i in range(1, len(arr)):
    l[i] += l[i-1]

for i in range(0, len(arr)):
    s += arr[i]*(l[-1]-l[i])

print(s%(10**9+7))