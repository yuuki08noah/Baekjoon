import sys
import heapq

input = sys.stdin.readline
n = int(input())
a = [64]
cnt = 0
if sum(a) == n:
    print(1)
while sum(a) > n:
    l = heapq.heappop(a)
    if sum(a) + l//2 > n:
        heapq.heappush(a, l//2)
    elif sum(a) + l//2 < n:
        heapq.heappush(a, l//2)
        heapq.heappush(a, l//2)
    else:
        print(len(a)+1)
        break
