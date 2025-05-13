import math
import sys
from collections import defaultdict

input = sys.stdin.readline
n = int(input())
arr = [0] + list(map(int, input().split()))
q = int(input())
b = int(math.sqrt(n))
queries = sorted([(tuple(map(int, input().split())), i) for i in range(q)], key=lambda x: (x[0][0]//b, x[0][1]))
appeared = defaultdict(int)
freq = [0] * 100001
cnt = 0
results = [0] * q
left, right = queries[0][0]

def add(idx):
    global cnt
    if appeared[arr[idx]] > 0:
        freq[appeared[arr[idx]]] -= 1
    appeared[arr[idx]] += 1
    freq[appeared[arr[idx]]] += 1
    cnt = max(cnt, appeared[arr[idx]])

def remove(idx):
    global cnt
    if appeared[arr[idx]] > 0:
        freq[appeared[arr[idx]]] -= 1
    appeared[arr[idx]] -= 1
    freq[appeared[arr[idx]]] += 1
    while cnt > 0 and freq[cnt] == 0:
        cnt -= 1

def get_max():
    return cnt

for i in range(left, right+1):
    add(i)

results[queries[0][1]] = get_max()
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

    results[idx] = get_max()
print(*results, sep='\n')