import math
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
arr = [0] + list(map(int, input().split()))
q = int(input())
b = int(math.sqrt(n))
queries = sorted([(tuple(map(int, input().split())), i) for i in range(q)], key=lambda x: (x[0][0]//b, x[0][1]))
appeared = [0] * (m+1)
freq = [0] * (n+1)
start, end = queries[0][0][0], queries[0][0][0]-1
results = [0] * q

def remove(x):
    appeared[arr[x]] -= 1

def add(x):
    appeared[arr[x]] += 1

def check():
    for i in range(1, m+1):
        if appeared[i] > (right - left + 1)//2:
            return i
    return 0
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
    res = check()
    if res == 0: results[idx] = "no"
    else: results[idx] = f"yes {res}"
print(*results, sep='\n')
