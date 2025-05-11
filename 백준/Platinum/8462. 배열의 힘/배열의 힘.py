import math
import sys

input = sys.stdin.readline
n, q = map(int, input().split())
arr = [0] + list(map(int, input().split()))
b = int(math.sqrt(n))
queries = sorted([(tuple(map(int, input().split())), i) for i in range(q)], key=lambda x: (x[0][0]//b, x[0][1]))
appeared = [0] * (max(arr)+1)
start, end = queries[0][0][0], queries[0][0][0]-1
cnt = 0
results = [0] * q
for query, idx in queries:
    left, right = query
    while start < left:
        cnt -= appeared[arr[start]] * appeared[arr[start]] * arr[start]
        appeared[arr[start]] -= 1
        cnt += appeared[arr[start]] * appeared[arr[start]] * arr[start]
        start += 1
    while start > left:
        start -= 1
        cnt -= appeared[arr[start]] * appeared[arr[start]] * arr[start]
        appeared[arr[start]] += 1
        cnt += appeared[arr[start]] * appeared[arr[start]] * arr[start]
    while end < right:
        end += 1
        cnt -= appeared[arr[end]] * appeared[arr[end]] * arr[end]
        appeared[arr[end]] += 1
        cnt += appeared[arr[end]] * appeared[arr[end]] * arr[end]
    while end > right:
        cnt -= appeared[arr[end]] * appeared[arr[end]] * arr[end]
        appeared[arr[end]] -= 1
        cnt += appeared[arr[end]] * appeared[arr[end]] * arr[end]
        end -= 1
    results[idx] = cnt
print(*results, sep='\n')
