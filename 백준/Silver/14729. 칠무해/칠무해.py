import sys
import math
import heapq

input = sys.stdin.readline
sum = 0
n = int(input())
pq = []
for i in range(n):
    heapq.heappush(pq, float(input()))
for i in range(7):
    print("{:.3f}".format(heapq.heappop(pq)))