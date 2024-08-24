import sys
import heapq

input = sys.stdin.readline
t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    arr.sort(reverse=False)
    ans = [1]
    while len(arr) != 1:
        val = heapq.heappop(arr) * heapq.heappop(arr)
        heapq.heappush(arr, val)
        ans.append((val*ans[-1])%(10**9+7))

    print(ans[-1]%(10**9+7))
