import sys
from collections import deque
import heapq

input = sys.stdin.readline
n = int(input())
for _ in range(n):
    k = list(map(str, input().strip()))
    num = int(''.join(k))
    cnt = 0
    while num != 6174:
        num = int(''.join(sorted(k, reverse=True))) - int(''.join(sorted(k, reverse=False)))
        k = list(map(str, str(num)))
        if len(k) != 4:
            k.insert(0, '0')
        cnt += 1
    print(cnt)