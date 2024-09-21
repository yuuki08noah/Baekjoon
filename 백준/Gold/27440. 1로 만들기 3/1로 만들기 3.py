import sys
from collections import deque
import heapq

input = sys.stdin.readline
n = int(input())
dp = {}
queue = [(0, n)]
while queue:
    depth, x = heapq.heappop(queue)
    if x in dp:
        continue

    dp.update({x: depth})
    if x == 1:
        break
    if x % 3 == 0 and x // 3 not in dp:
        heapq.heappush(queue, (depth + 1, x // 3))
    if x % 2 == 0 and x // 2 not in dp:
        heapq.heappush(queue, (depth + 1, x // 2))
    if x > 1 and x - 1 not in dp:
        heapq.heappush(queue, (depth + 1, x - 1))

print(dp[1])