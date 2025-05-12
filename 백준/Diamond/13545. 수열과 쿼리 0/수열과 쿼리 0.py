import sys
import math
from collections import deque

input = sys.stdin.readline
n = int(input())
arr = [n] + list(map(int, input().split()))
for i in range(1, n+1): arr[i] += arr[i-1]
q = int(input())
b = int(math.ceil(math.sqrt(n)))
queries = []
for i in range(q):
    l, r = map(int, input().split())
    queries.append(((l-1, r), i))
queries.sort(key=lambda x: (x[0][0]//b, x[0][1]))
# print(queries)
start, end = queries[0][0][0], queries[0][0][1]
index = [deque() for _ in range(200100)]
freq = [0 for _ in range(200100)]
sqrt_freq = [0 for _ in range(b+200)]

def add(x, idx, dir):
    dq = index[x]
    if len(dq) >= 2:
        prev_dist = dq[-1] - dq[0]
        freq[prev_dist] -= 1
        sqrt_freq[prev_dist//b] -= 1
    if dir: dq.appendleft(idx)
    else: dq.append(idx)
    new_dist = dq[-1] - dq[0]
    freq[new_dist] += 1
    sqrt_freq[new_dist//b] += 1

def remove(x, dir):
    dq = index[x]
    if not dq:
        return
    if len(dq) >= 2:
        prev_dist = dq[-1] - dq[0]
        freq[prev_dist] -= 1
        sqrt_freq[prev_dist//b] -= 1

    if dir: dq.popleft()
    else: dq.pop()

    if len(dq) >= 2:
        new_dist = dq[-1] - dq[0]
        freq[new_dist] += 1
        sqrt_freq[new_dist//b] += 1

def get_max():
    for i in range(len(sqrt_freq)-1, -1, -1):
        if sqrt_freq[i] > 0:
            start = (i+1)*b - 1
            end = i*b
            for j in range(start, end-1, -1):
                if j < len(freq) and freq[j] > 0:
                    return j
    return 0
results = [0] * q
left, right = queries[0][0]

for i in range(left, right+1):
    add(arr[i], i, False)

results[queries[0][1]] = get_max()

for query, idx in queries[1:]:
    left, right = query
    while start > left:
        start -= 1
        add(arr[start], start, True)
    while end < right:
        end += 1
        add(arr[end], end, False)
    while start < left:
        remove(arr[start], True)
        start += 1
    while end > right:
        remove(arr[end], False)
        end -= 1
    results[idx] = get_max()

print(*results, sep='\n')
