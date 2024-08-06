import sys
from collections import deque
import random
import math


input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
deque = deque()
deque.append(arr[0])
print(deque[0], end=' ')
for i in range(1, n):
    while len(deque) > 0 and arr[i] < deque[-1]:
        deque.pop()
    deque.append(arr[i])
    if i >= m and deque[0] == arr[i - m]:
        deque.popleft()
    print(deque[0], end=' ')
