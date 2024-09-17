import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
cnt = 1
for i in range(len(arr)-1):
    if arr[i] <= arr[i+1]:
        cnt += 1
print(cnt)