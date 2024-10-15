import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
arr = sorted(list(map(int, input().split())))
m = int(input())
find = list(map(int, input().split()))

def binary_search(target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return True
        if arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False

for i in find:
    print(int(binary_search(i,0, n - 1)))
