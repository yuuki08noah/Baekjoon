import sys
input = sys.stdin.readline

n = int(input())
arr = sorted([sum(list(map(int, input().split()))[1:]) for i in range(n)])
for i in range(1, n):
    arr[i] += arr[i-1]
print(sum(arr))