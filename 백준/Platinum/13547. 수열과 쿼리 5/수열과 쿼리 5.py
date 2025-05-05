import math
import sys

input = sys.stdin.readline
n = int(input())
arr = [0] + list(map(int, input().split()))
q = int(input())
b = int(math.sqrt(n))
queries = sorted([(tuple(map(int, input().split())), i) for i in range(q)], key=lambda x: (x[0][0]//b, x[0][1]))
appeared = [0] * (max(arr)+1)
start, end = queries[0][0][0], queries[0][0][0]-1
cnt = 0
results = [0] * q
for query, idx in queries:
    left, right = query
    while start < left:
        appeared[arr[start]] -= 1
        if appeared[arr[start]] == 0: cnt -= 1
        start += 1
    while start > left:
        start -= 1
        appeared[arr[start]] += 1
        if appeared[arr[start]] == 1: cnt += 1
    while end < right:
        end += 1
        appeared[arr[end]] += 1
        if appeared[arr[end]] == 1: cnt += 1
    while end > right:
        appeared[arr[end]] -= 1
        if appeared[arr[end]] == 0: cnt -= 1
        end -= 1
    results[idx] = cnt
print(*results, sep='\n')
