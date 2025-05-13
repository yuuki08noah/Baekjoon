import math
import sys

input = sys.stdin.readline
n, q = map(int, input().split())
arr = [0] + list(map(int, input().split()))
b = int(math.sqrt(n))
queries = sorted([(tuple(map(int, input().split())), i) for i in range(q)], key=lambda x: (x[0][0]//b, x[0][1]))
appeared = [0] * (100001)
cnt = 0
results = [0] * q
left, right = queries[0][0]
for i in range(left, right+1):
    appeared[arr[i]] += 1
    if appeared[arr[i]] == 3: cnt += 1

results[queries[0][1]] = cnt
start, end = queries[0][0][0], queries[0][0][1]
for query, idx in queries[1:]:
    left, right = query
    while start < left:
        appeared[arr[start]] -= 1
        if appeared[arr[start]] == 2: cnt -= 1
        start += 1
    while end > right:
        appeared[arr[end]] -= 1
        if appeared[arr[end]] == 2: cnt -= 1
        end -= 1
    while start > left:
        start -= 1
        appeared[arr[start]] += 1
        if appeared[arr[start]] == 3: cnt += 1
    while end < right:
        end += 1
        appeared[arr[end]] += 1
        if appeared[arr[end]] == 3: cnt += 1
    results[idx] = cnt
print(*results, sep='\n')
