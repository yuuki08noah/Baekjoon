import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
arr = sorted(list(map(int, input().split())))
m = int(input())
find = list(map(int, input().split()))

def binary_search(target, start, end):
    mid = (start + end) // 2
    if arr[mid] == target:
        return True

    if start > end:
        return False

    if arr[mid] > target:
        return binary_search(target, start, mid - 1)
    else:
        return binary_search(target, mid + 1, end)

for i in find:
    print(int(binary_search(i,0, n - 1)))
