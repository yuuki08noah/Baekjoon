import sys
import math
from bisect import bisect_left

def isPal(n):
    n = str(n)
    i = 0
    while len(n) - i - 1 >= i:
        if n[-i-1] != n[i]:
            return False
        else:
            i += 1
            continue
    return True

input = sys.stdin.readline
n = int(input())
arr = [False] * 10000001
arr[1] = True
arr[0] = True
for i in range(2, 3164):
    if arr[i] == False:
        for j in range(i*2, 10000001, i):
            arr[j] = True

for i in range(10000001):
    if not arr[i]:
        if isPal(i) and i >= n:
            print(i)
            break