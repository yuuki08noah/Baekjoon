import sys
import heapq

input = sys.stdin.readline
n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
print(arr[-m])