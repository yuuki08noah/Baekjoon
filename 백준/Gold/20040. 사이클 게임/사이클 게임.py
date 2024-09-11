import sys
from collections import deque
import heapq

input = sys.stdin.readline
n, m = map(int, input().split())

parents = [-1 for i in range(n+1)]
rank = [1] * (n+1)
def union(a, b):
    if find(a) == find(b):
        return False
    else:
        root_a = find(a)
        root_b = find(b)
        if rank[root_a] < rank[root_b]:
            parents[root_a] = root_b
        elif rank[root_a] >= rank[root_b]:
            parents[root_b] = root_a
            rank[root_a] += 1
        return True

def find(x):
    if parents[x] == -1:
        return x
    parents[x] = find(parents[x])
    return parents[x]

for i in range(m):
    x, y = map(int, input().split())
    if not union(x, y):
        print(i+1)
        exit()

print(0)