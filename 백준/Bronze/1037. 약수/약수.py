import sys

input = sys.stdin.readline
n = int(input())
arr = sorted(map(int, input().split()))
print(arr[n//2]*arr[n-n//2-1])