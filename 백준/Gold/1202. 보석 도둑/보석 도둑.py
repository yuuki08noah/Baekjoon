import decimal
import sys
import math
import heapq

input = sys.stdin.readline
n, k = map(int, input().split())
jewels = []
bags = []
for i in range(n):
    jewels.append(list(map(int, input().split())))
for i in range(k):
    bags.append(int(input()))

jewels.sort(key=lambda x: (x[0], x[1]))
bags.sort()
sum = 0

PriorityQueue = []
j = 0
for i in bags:
    while j < len(jewels) and jewels[j][0]<=i:
        heapq.heappush(PriorityQueue, -jewels[j][1])
        j += 1
    if len(PriorityQueue) != 0:
        sum -= heapq.heappop(PriorityQueue)

print(sum)