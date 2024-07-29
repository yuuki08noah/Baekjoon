import random
import math
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
A = set()
B = set()
for i in range(n):
    A.add(a[i])
for i in range(m):
    B.add(b[i])
C = list(A-B)
C.sort()
print(len(C))
print(*C)