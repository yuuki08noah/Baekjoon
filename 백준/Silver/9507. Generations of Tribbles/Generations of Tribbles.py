import sys
from collections import deque
import heapq
t = int(input())
koong = [1, 1, 2, 4]
for i in range(68):
    koong.append(koong[-1] + koong[-2] + koong[-3] + koong[-4])

for i in range(t):
    n = int(input())
    print(koong[n])