import sys
from collections import deque
import heapq

input = sys.stdin.readline
t = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

B_map = {}
for i in range(1, n):
    A[i] += A[i - 1]
for i in range(1, m):
    B[i] += B[i - 1]

for i in range(m):
    if B[i] in B_map:
        B_map[B[i]] += 1
    else:
        B_map[B[i]] = 1
    for j in range(i):
        if B[i]-B[j] in B_map:
            B_map[B[i]-B[j]] += 1
        else:
            B_map[B[i] - B[j]] = 1

cnt = 0
for i in range(n):
    cnt += B_map[t - A[i]] if t - A[i] in B_map else 0
    for j in range(i):
        cnt += B_map[t - (A[i]-A[j])] if t - (A[i]-A[j]) in B_map else 0
print(cnt)
