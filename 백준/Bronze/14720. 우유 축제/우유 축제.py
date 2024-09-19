import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
cnt = 0
try:
    i = arr.index(0)
except:
    print(0)
    exit()
while i < n:
    temp = arr[i]
    while i < n and arr[i] != (temp + 1)%3:
        i += 1
    cnt += 1
print(cnt)