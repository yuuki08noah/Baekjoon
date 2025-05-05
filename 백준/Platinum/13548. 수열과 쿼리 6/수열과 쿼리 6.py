import math
import sys

input = sys.stdin.readline
n = int(input())
arr = [0] + list(map(int, input().split()))
q = int(input())
b = int(math.sqrt(n))
queries = sorted([(tuple(map(int, input().split())), i) for i in range(q)], key=lambda x: (x[0][0]//b, x[0][1]))
appeared = [0] * (max(arr)+1)
freq = [0] * (n+1)
start, end = queries[0][0][0], queries[0][0][0]-1
cnt = 0
results = [0] * q
def remove(x):
    global cnt, freq
    freq[appeared[arr[x]]] -= 1
    old_freq = appeared[arr[x]]
    appeared[arr[x]] -= 1
    freq[appeared[arr[x]]] += 1
    if old_freq == cnt and freq[old_freq] == 0:
        cnt = old_freq - 1

def add(x):
    global cnt
    freq[appeared[arr[x]]] -= 1
    appeared[arr[x]] += 1
    freq[appeared[arr[x]]] += 1
    cnt = max(cnt, appeared[arr[x]])

for query, idx in queries:
    left, right = query
    while start < left:
        remove(start)
        start += 1
    while end > right:
        remove(end)
        end -= 1
    while start > left:
        start -= 1
        add(start)
    while end < right:
        end += 1
        add(end)
    results[idx] = cnt
print(*results, sep='\n')
