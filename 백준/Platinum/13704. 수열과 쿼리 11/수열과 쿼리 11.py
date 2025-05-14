import math
import sys
from collections import defaultdict

input = sys.stdin.readline
n, k = map(int, input().split())
arr = [0] + list(map(int, input().split()))
q = int(input())
b = int(math.sqrt(n))
queries = sorted(
    [((l - 1, r), i) for i, (l, r) in enumerate(tuple(map(int, input().split()) for _ in range(q)))],
    key=lambda x: (x[0][0] // b, x[0][1])
)

cnt = 0
results = [0] * q
left, right = queries[0][0]
freq = defaultdict(int)
prefix = [0] * 200001
for i in range(1, n+1): prefix[i] = prefix[i-1] ^ arr[i]

def add(idx):
    global cnt
    val = prefix[idx]
    cnt += freq[val ^ k]
    freq[val] += 1


def remove(idx):
    global cnt
    val = prefix[idx]
    freq[val] -= 1
    cnt -= freq[val ^ k]

for i in range(left, right+1):
    add(i)
results[queries[0][1]] = cnt
start, end = queries[0][0]
for query, idx in queries[1:]:
    left, right = query
    while start > left:
        start -= 1
        add(start)
    while end < right:
        end += 1
        add(end)
    while start < left:
        remove(start)
        start += 1
    while end > right:
        remove(end)
        end -= 1

    results[idx] = cnt
print(*results, sep='\n')