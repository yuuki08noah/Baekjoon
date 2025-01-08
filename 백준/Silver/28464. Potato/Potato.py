import sys

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
arr.sort()
mid = len(arr)//2
print(sum(arr[:mid]), sum(arr[mid:]))