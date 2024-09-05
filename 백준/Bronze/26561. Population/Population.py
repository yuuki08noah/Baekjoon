import sys
from collections import deque
import heapq

input = sys.stdin.readline
k = int(input())
for i in range(k):
    n, m = map(int, input().split())
    print(n + m // 4 - m // 7)