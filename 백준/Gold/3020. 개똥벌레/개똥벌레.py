import sys
import bisect

input = sys.stdin.readline
n, h = map(int, input().split())
arr = [int(input()) for _ in range(n)]
bottom = sorted([arr[i] for i in range(len(arr)) if i % 2 == 0])
top = sorted([h - arr[i] for i in range(len(arr)) if i % 2 == 1])
bottom_h = []
top_h = []
for i in range(h):
    bottom_h.append(n//2 - bisect.bisect_left(bottom, i + 1))
    top_h.append(bisect.bisect_left(top, i + 1))

k = bottom_h[0] + top_h[0]
cnt = 1
for i in range(1, h):
    if k > bottom_h[i] + top_h[i]:
        k = bottom_h[i] + top_h[i]
        cnt = 1
    elif k == bottom_h[i] + top_h[i]:
        cnt += 1
print(k, cnt)